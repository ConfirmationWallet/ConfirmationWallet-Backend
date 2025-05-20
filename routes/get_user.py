from helper_functions import supabase
from flask import Flask, request, jsonify


def get_user_from_session(request):
    user = supabase.get_user_from_session(request)
    if user:
        return user
    else:
        return {"error": "User not found"}, 401
