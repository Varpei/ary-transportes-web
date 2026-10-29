#!/usr/bin/env bash
set -e

if [ ! -d .git ]; then
  git init -b main
fi

if [ ! -f .gitignore ]; then
  printf "__pycache__/\\n.DS_Store\\n.env\\n" > .gitignore
fi

git add -A
if ! git diff --cached --quiet; then
  git commit -m "feat: prototipo blindado ARY Transportes pronto para Codespaces"
fi

if ! git remote get-url origin >/dev/null 2>&1; then
  if gh auth status >/dev/null 2>&1; then
    gh repo create ary-transportes-web --public --source=. --remote=origin --push
  else
    echo "GitHub CLI não autenticado; configure 'gh auth login' para publicar." >&2
  fi
else
  git push -u origin main
fi

if [ -n "${CODESPACE_NAME:-}" ]; then
  gh codespace ports visibility 8080:public -c "$CODESPACE_NAME" || true
fi
