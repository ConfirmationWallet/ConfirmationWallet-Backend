import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")


def get_user_from_session(request):
    supabase: Client = create_client(supabase_url, supabase_key)
    session = request.headers.get("Authorization")
    if not session:
        return None
    session_token = session[len("Bearer ") :]
    user = supabase.auth.get_user(session_token)
    return user.user
