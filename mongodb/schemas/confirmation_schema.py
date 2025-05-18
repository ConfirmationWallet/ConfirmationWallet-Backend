# from pymongo import MongoClient
# from bson.objectid import ObjectId
# from datetime import datetime
# import os
# from dotenv import load_dotenv

# load_dotenv()
# MONGODB_URI = os.getenv("MONGODB_URI")

# # Connect to MongoDB
# client = MongoClient(MONGODB_URI)
# db = client["ConfirmationWallet"]

# # print("client: ", client["confirmationWallet"])


# itinerary_schema = {
#     "$jsonSchema": {
#         "bsonType": "object",
#         "required": [
#             "booking_date",
#             "event_date",
#             "event_time",
#             "email",
#             "confirmation_number",
#         ],
#         "properties": {
#             "user": {
#                 "bsonType": "string",
#                 "description": "must be the _id of the user from SQL db and is required",
#             },
#             "booking_date": {
#                 "bsonType": "date",
#                 "description": "must be a date and is required",
#             },
#             "event_date": {
#                 "bsonType": "date",
#                 "description": "must be a date and is required",
#             },
#             "event_time": {
#                 "bsonType": "date",
#                 "description": "must be a date and is required",
#             },
#             "email": {
#                 "bsonType": "string",
#                 "description": "must be a string and is required",
#             },
#             "confirmation_number": {
#                 "bsonType": "string",
#                 "description": "must be a string and is required",
#             },
#             "details": {
#                 "bsonType": "object",
#                 "description": "must be an object and is not required",
#             },
#         },
#     }
# }

# test_first_confirmation = {
#     "user": "123456",
#     "booking_date": datetime.now(),
#     "event_date": datetime.now(),
#     "event_time": datetime.now(),
#     "email": "fakeEmail@fake.com",
#     "confirmation_number": "123456y",
#     "detailes": {"test": "test", "test2": "test2"},
# }

# # Create collection with validation
# try:
#     print("starting the collection build")
#     collection = db.create_collection("confirmations", validator=itinerary_schema)
#     print("adding document")
#     firstConfirmation = db["confirmations"].insert_one(test_first_confirmation)

# except Exception as e:
#     print(f"Error creating collection: {e}")
