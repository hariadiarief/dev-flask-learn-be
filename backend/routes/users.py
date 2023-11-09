from flask import Blueprint, jsonify, request, Response

users_bp = Blueprint("user", __name__, url_prefix="/users")

@users_bp.route("/", methods=["GET"])
def get_all_users():
    all_user = [
        {"id": 1, "name" : "bob"},
        {"id": 2, "name" : "joe"}
    ]
    # return jsonify(all_user)


@users_bp.route("/", methods=["POST"])
def create_user():
    # you can change request.json with {data | header | method | files | args}
    d = request.form
    print(d)
    return Response(status=204) 