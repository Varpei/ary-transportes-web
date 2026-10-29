"""Valida, inicializa e publica o projeto ARY Transportes via GitHub CLI."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    print("[AUTO-DEPLOY]", " ".join(command))
    return subprocess.run(command, cwd=ROOT, text=True, check=check)


def validate() -> None:
    python = shutil.which("python3") or sys.executable
    run([python, "-m", "py_compile", "app_codespaces.py", "scripts/process_media.py"])
    js_files = sorted((ROOT / "src" / "assets" / "js").glob("*.js"))
    node = shutil.which("node")
    if node:
        for path in js_files:
            run([node, "--check", str(path)])
    else:
        print("[AUTO-DEPLOY] node não encontrado; validação JS ignorada.")


def main() -> int:
    validate()
    if not (ROOT / ".git").exists():
        run(["git", "init", "-b", "main"])
    else:
        run(["git", "branch", "-M", "main"])
    run(["git", "add", "-A"])
    staged = subprocess.run(
        ["git", "diff", "--cached", "--quiet"], cwd=ROOT, check=False
    )
    if staged.returncode != 0:
        run(["git", "commit", "-m", "feat: infraestrutura zero-touch ARY Transportes"])

    remote = subprocess.run(
        ["git", "remote", "get-url", "origin"], cwd=ROOT, check=False,
        stdout=subprocess.DEVNULL,
    )
    gh = shutil.which("gh")
    if remote.returncode != 0:
        if not gh:
            print("[AUTO-DEPLOY] gh não encontrado; sincronização remota bloqueada.")
            return 2
        if subprocess.run(["gh", "auth", "status"], cwd=ROOT, check=False).returncode != 0:
            print("[AUTO-DEPLOY] gh não autenticado; execute gh auth login.")
            return 2
        run([
            "gh", "repo", "create", "ary-transportes-web", "--public",
            "--source=.", "--remote=origin", "--push",
        ])
    else:
        run(["git", "push", "-u", "origin", "main"])
    print("[AUTO-DEPLOY] Publicação concluída.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
