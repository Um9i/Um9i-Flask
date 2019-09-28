from flask import Blueprint, jsonify

bp = Blueprint("index", __name__)


@bp.route("/")
def index():
    return jsonify(hello="Hello, World!")
