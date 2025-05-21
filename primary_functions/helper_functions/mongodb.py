from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")


def get_mongodb_client():
    client = MongoClient(MONGODB_URI)
    db = client["ConfirmationWallet"]
    return db


def get_confirmations_collection():
    db = get_mongodb_client()
    confirmation_collection = db["confirmations"]
    return confirmation_collection


def add_confirmation(confirmation_data, user):
    confirmation_collection = get_confirmations_collection()

    # test_confirmation = {
    #     "user": user.id,
    #     "booking_date": datetime.now(),
    #     "event_date": datetime.now(),
    #     "event_time": datetime.now(),
    #     "email": "fakeEmail@fake.com",
    #     "confirmation_number": "123456y",
    #     "details": {"test5": "test5", "test6": "test6"},
    #     "active": True,
    # }

    try:
        result = confirmation_collection.insert_one(confirmation_data)
        print("Inserted confirmation:", result.inserted_id)
    except Exception as e:
        print("Error inserting confirmation:", e)
        return e

    return result.inserted_id


def deactivate_confirmation(confirmation_id):
    confirmation_collection = get_confirmations_collection()

    try:
        result = confirmation_collection.update_one(
            {"_id": confirmation_id}, {"$set": {"active": False}}
        )
        print("Deactivated confirmation:", result.modified_count)
    except Exception as e:
        print("Error deactivating confirmation:", e)
        return e

    return result.modified_count


def activate_confirmation(confirmation_id):
    confirmation_collection = get_confirmations_collection()

    try:
        result = confirmation_collection.update_one(
            {"_id": confirmation_id}, {"$set": {"active": True}}
        )
        print("Deactivated confirmation:", result.modified_count)
    except Exception as e:
        print("Error deactivating confirmation:", e)
        return e

    return result.modified_count
