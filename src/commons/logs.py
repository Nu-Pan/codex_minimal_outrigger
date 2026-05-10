"""cmot のレポート保存処理。"""

from datetime import datetime
from pathlib import Path


def new_log_path(repo_root: Path, category: str) -> Path:
    """指定 category のログファイル path を生成する。

    Args:
        repo_root: 操作対象 repository root。
        category: .cmot/logs 配下の分類名。

    Returns:
        新規ログファイル path。
    """
    log_dir = repo_root / ".cmot" / "logs" / category
    log_dir.mkdir(parents=True, exist_ok=True)

    # 秒単位の衝突を避けるため microsecond まで含める。
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
    return log_dir / f"{timestamp}.md"
