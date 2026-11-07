#!/usr/bin/env python3
"""
Servidor HTTP Blindado com Live-Reload Nativo — ARY Transportes e Viagens
Compatível com Windows (py -3), GitHub Codespaces (Porta 8080 Public) e Render ($PORT).
Expõe /healthz, /api/status e /__mtime (para atualização em tempo real no localhost).
"""
import http.server
import json
import os
import socketserver
from datetime import datetime, timezone
from pathlib import Path

PORT = int(os.environ.get("PORT", 8080))
ROOT_DIR = Path(__file__).resolve().parent
SRC_DIR = ROOT_DIR / "src"

CSP_POLICY = (
    "default-src 'self'; "
    "script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com https://www.googletagmanager.com; "
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
    "font-src 'self' https://fonts.gstatic.com data:; "
    "img-src 'self' data: https:; "
    "connect-src 'self' https://www.google-analytics.com; "
    "frame-ancestors 'none'; "
    "base-uri 'self'; "
    "form-action 'self' https://wa.me;"
)


def get_latest_mtime(directory: Path) -> float:
    latest = 0.0
    if not directory.exists():
        return latest
    for root, _, files in os.walk(directory):
        for fname in files:
            if fname.endswith((".html", ".css", ".js", ".json", ".webp")):
                try:
                    mtime = os.path.getmtime(os.path.join(root, fname))
                    if mtime > latest:
                        latest = mtime
                except OSError:
                    pass
    return latest


class HardenedARYHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".webp": "image/webp",
        ".json": "application/json",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SRC_DIR), **kwargs)

    def log_message(self, format, *args):
        if self.path and self.path.startswith("/__mtime"):
            return
        super().log_message(format, *args)

    def end_headers(self):
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header(
            "Permissions-Policy",
            "accelerometer=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=()",
        )
        self.send_header("X-XSS-Protection", "1; mode=block")
        self.send_header("Strict-Transport-Security", "max-age=31536000; includeSubDomains")
        self.send_header("Content-Security-Policy", CSP_POLICY)
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        super().end_headers()

    def do_GET(self):
        clean_path = self.path.split("?")[0]
        if clean_path == "/__mtime":
            payload = json.dumps({"mtime": get_latest_mtime(SRC_DIR)}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return

        if clean_path in ("/healthz", "/api/status"):
            payload = json.dumps(
                {
                    "status": "ok",
                    "project": "ary-transportes-web",
                    "live_reload": True,
                    "security": "CSP + HSTS + XFO + NoSniff enforced",
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                },
                ensure_ascii=False,
            ).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        super().do_GET()


class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
    os.makedirs(SRC_DIR, exist_ok=True)
    with ThreadingHTTPServer(("0.0.0.0", PORT), HardenedARYHandler) as httpd:
        print(f"[ARY-LIVE-SERVER] Online em http://localhost:{PORT}")
        print(f"[ARY-LIVE-SERVER] Live-Reload ativo em http://localhost:{PORT}/__mtime")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[ARY-SERVER] Servidor encerrado com seguranca.")


if __name__ == "__main__":
    main()
