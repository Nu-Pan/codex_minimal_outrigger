"""Codex CLI 呼び出しの共通処理。"""

import json
import subprocess
from collections.abc import Callable
from pathlib import Path

from .errors import CmocError
from .timestamps import make_timestamp


def run_codex_exec(
    repo_root: Path,
    prompt: str,
    *,
    read_only: bool,
    expect_json: bool = False,
    output_schema: dict[str, object] | None = None,
    json_validator: Callable[[object], None] | None = None,
) -> str:
    """`codex exec` を実行し、フルログを `.cmoc/logs` に保存する。"""
    log_dir = repo_root / ".cmoc" / "logs" / "codex_exec"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{make_timestamp()}.log"
    command = ["codex", "exec"]
    if read_only:
        command.extend(["--sandbox", "read-only"])
    else:
        command.extend(["--sandbox", "workspace-write"])
    schema_path = _write_output_schema(log_path, output_schema)
    if schema_path is not None:
        command.extend(["--output-schema", str(schema_path)])
    command.append(prompt)

    # Structured Output 相当の JSON が必要な呼び出しだけ最大 3 回リトライする。
    attempts = 3 if expect_json else 1
    last_stdout = ""
    last_stderr = ""
    last_json_error = ""
    for attempt in range(1, attempts + 1):
        result = subprocess.run(
            command,
            cwd=repo_root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        last_stdout = result.stdout
        last_stderr = result.stderr
        _append_codex_log(log_path, command, prompt, attempt, result, schema_path)

        if result.returncode != 0:
            raise CmocError(
                "codex exec failed.",
                [
                    "Read the codex exec log.",
                    "Fix the underlying Codex CLI or repository error, then run cmoc again.",
                ],
                f"Log: {log_path}\nSTDERR:\n{result.stderr}",
                result.returncode,
            )

        if not expect_json:
            return result.stdout

        try:
            value = json.loads(result.stdout)
            if json_validator is not None:
                json_validator(value)
            return result.stdout
        except (json.JSONDecodeError, ValueError) as error:
            last_json_error = str(error)
            continue

    raise CmocError(
        "codex exec did not return valid JSON matching schema after retries.",
        [
            "Read the codex exec log.",
            "Adjust the prompt or fake Codex CLI output, then run cmoc again.",
        ],
        "\n".join(
            [
                f"Log: {log_path}",
                f"Output schema: {schema_path}" if schema_path is not None else "Output schema: none",
                f"Last JSON error: {last_json_error}",
                "Last stdout:",
                last_stdout,
                "Last stderr:",
                last_stderr,
            ]
        ),
    )


def parse_json_object(raw: str) -> dict[str, object]:
    """Codex CLI の JSON 応答を object として読む。"""
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise CmocError(
            "codex exec returned JSON that is not an object.",
            ["Fix the Codex CLI output schema.", "Run cmoc again."],
            raw,
        )
    return value


def _append_codex_log(
    log_path: Path,
    command: list[str],
    prompt: str,
    attempt: int,
    result: subprocess.CompletedProcess[str],
    schema_path: Path | None,
) -> None:
    """1 回分の Codex CLI 呼び出し情報をフルログへ追記する。"""
    content = [
        f"attempt: {attempt}",
        f"command: {' '.join(command[:-1])} <prompt>",
        f"output_schema: {schema_path}" if schema_path is not None else "output_schema: none",
        "prompt:",
        prompt,
        f"returncode: {result.returncode}",
        "stdout:",
        result.stdout,
        "stderr:",
        result.stderr,
        "",
    ]
    with log_path.open("a", encoding="utf-8") as log_file:
        log_file.write("\n".join(content))


def _write_output_schema(log_path: Path, output_schema: dict[str, object] | None) -> Path | None:
    """Structured Output 用 JSON schema をログ配下へ保存する。"""
    if output_schema is None:
        return None
    schema_dir = log_path.parent / "schemas"
    schema_dir.mkdir(parents=True, exist_ok=True)
    schema_path = schema_dir / f"{log_path.stem}.schema.json"
    schema_path.write_text(
        json.dumps(output_schema, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return schema_path
