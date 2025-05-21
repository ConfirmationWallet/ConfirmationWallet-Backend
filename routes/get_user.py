from primary_functions.authentication import get_user
from flask import Flask, request, jsonify


def get_user_from_session(request):
    user = get_user.get_user_from_session(request)
    if user:
        return user
    else:
        return {"error": "User not found"}, 401
