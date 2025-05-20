from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
db = client["ConfirmationWallet"]

# print("client: ", client["confirmationWallet"])


confirmation_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [
            "booking_date",
            "event_date",
            "event_time",
            "email",
            "confirmation_number",
            "active",
        ],
        "properties": {
            "_id": {
                "bsonType": "objectId",
                "description": "must be an objectId and is not required",
            },
            "user": {
                "bsonType": "string",
                "description": "must be the _id of the user from SQL db and is required",
            },
            "booking_date": {
                "bsonType": ["date", "null"],
                "description": "must be a date and is required",
            },
            "event_date": {
                "bsonType": ["date", "null"],
                "description": "must be a date and is required",
            },
            "event_time": {
                "bsonType": ["date", "null"],
                "description": "must be a date and is required",
            },
            "email": {
                "bsonType": ["string", "null"],
                "description": "must be a string and is required",
            },
            "confirmation_number": {
                "bsonType": ["string", "null"],
                "description": "must be a string and is required",
            },
            "details": {
                "bsonType": ["object", "null"],
                "description": "must be an object and is not required",
            },
            "active": {
                "bsonType": "bool",
                "description": "must be a boolean and is not required",
            },
        },
        "additionalProperties": False,
    }
}
try:
    confirmations_collection = db["confirmations"]
    command_result = db.command(
        "collMod",
        "confirmations",
        validator=confirmation_schema,
        validationLevel="strict",  # Apply validation strictly to all operations
        validationAction="error",  # Reject documents that fail validation
    )

    print(f"Validator amended successfully: {command_result}")

except Exception as e:
    print(f"Error amending validator: {e}")
