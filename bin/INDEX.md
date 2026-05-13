# `cmoc`

## Summary

- Bash executable entrypoint for the cmoc CLI.
- Resolves the cmoc repository root from the script location.
- Executes the repository-local virtualenv Python interpreter at `.venv/bin/python` with `src/main.py`, forwarding all command-line arguments.

## Read this when

- You need to understand how the installed or checked-out `cmoc` command launches the Python implementation.
- You are debugging failures before `src/main.py` starts, such as missing virtualenv interpreter, wrong repository root detection, or shell entrypoint issues.
- You are changing packaging, local execution, or command shim behavior for the `cmoc` executable.

## Do not read this when

- You need to understand cmoc command behavior after startup; read the implementation under `src` instead.
- You are looking for user-facing CLI options, subcommands, prompts, or workflow logic.
- You are working on tests, specifications, or documentation unrelated to the executable launcher.

## hash

- ce41b0e4112e297abd3d35376a1dc555dcd532748b6942cf7368f2ad0c72b072
