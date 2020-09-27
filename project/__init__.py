from flask import Flask, render_template
from werkzeug.utils import find_modules, import_string


def create_app(config=None):
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    register_blueprints(app)
    return app


def page_not_found(e):
  return render_template("404.html"), 404


def register_blueprints(app):
    for name in find_modules("project.blueprints"):
        mod = import_string(name)
        if hasattr(mod, "bp"):
            app.register_blueprint(mod.bp)
    return None
