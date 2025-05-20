import os
from datetime import datetime
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(supabase_url, supabase_key)


def signin_with_email_password(request):
    email = request.form.get("email")
    password = request.form.get("password")

    response = supabase.auth.sign_in_with_password(
        {"email": email, "password": password}
    )

    print(
        "type of converted date: ", type(datetime.fromisoformat("2025-02-28T00:00:00"))
    )

    return response


def signin_with_phone_password(request):
    phone = request.form.get("phone")
    password = request.form.get("password")

    response = supabase.auth.sign_in_with_password(
        {"phone": phone, "password": password}
    )

    return response
