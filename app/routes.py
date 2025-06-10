from flask import Blueprint, request, jsonify
from .models import Result
from . import db

bp = Blueprint('main', __name__)  # ← ВАЖНО: без этого не будет работать

@bp.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok"})

@bp.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    name = data.get("name")
    score = data.get("score")

    if not name or not isinstance(score, int):
        return jsonify({"error": "Invalid input"}), 400

    result = Result(name=name, score=score)
    db.session.add(result)
    db.session.commit()
    return jsonify({"message": "Data submitted"}), 201

@bp.route("/results", methods=["GET"])
def results():
    results = Result.query.all()
    return jsonify([
        {
            "id": r.id,
            "name": r.name,
            "score": r.score,
            "timestamp": r.timestamp.isoformat()
        } for r in results
    ])
