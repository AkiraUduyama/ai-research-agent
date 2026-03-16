import sys, os, traceback

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

_err = None
try:
    from gui_app import app
    try:
        from gui_app import migrate_config
        migrate_config()
    except Exception:
        pass
except Exception:
    _err = traceback.format_exc()
    from flask import Flask
    app = Flask(__name__)
    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def catch_all(path):
        return "<pre>" + (_err or "unknown") + "</pre>", 500
