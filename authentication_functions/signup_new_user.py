import os

from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')

supabase: Client = create_client(supabase_url, supabase_key)

def signup_with_email_password(request):
    email = request.form.get('email')
    password = request.form.get('password')
    
    response = supabase.auth.sign_up(
        {
            'email': email,
            'password': password
        }
    )

    return response

def signup_with_phone_password(request):
    phone = request.form.get('phone')
    password = request.form.get('password')
    
    response = supabase.auth.sign_up(
        {
            'phone': phone,
            'password': password
        }
    )

    return response