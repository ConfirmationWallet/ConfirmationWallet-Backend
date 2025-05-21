from primary_functions.helper_functions.mongodb import get_confirmations_collection
from primary_functions.authentication.get_user import get_user_from_session


def get_all_confirmations_by_user(request):
    print("get_all_confirmations_by_user")
    user = get_user_from_session(request)
    if not user:
        return {"error": "User not found"}, 401

    confirmation_collection = get_confirmations_collection()
    confirmations_cursor = confirmation_collection.find({"user": user.id})
    confirmations_list = []
    for doc in confirmations_cursor:
        # Convert ObjectId to string for JSON serialization
        if "_id" in doc:
            doc["_id"] = str(doc["_id"])
        confirmations_list.append(doc)

    return confirmations_list


def get_active_confirmations_by_user(request):
    user = get_user_from_session(request)
    if not user:
        return {"error": "User not found"}, 401

    confirmation_collection = get_confirmations_collection()
    confirmations_cursor = confirmation_collection.find(
        {"user": user.id, "active": True}
    )
    confirmations_list = []
    for doc in confirmations_cursor:
        # Convert ObjectId to string for JSON serialization
        if "_id" in doc:
            doc["_id"] = str(doc["_id"])
        confirmations_list.append(doc)

    return confirmations_list

    return confirmations_query_result


def get_inactive_confirmations_by_user(request):
    user = get_user_from_session(request)
    if not user:
        return {"error": "User not found"}, 401

    confirmation_collection = get_confirmations_collection()
    confirmations_cursor = confirmation_collection.find(
        {"user": user.id, "active": False}
    )
    confirmations_list = []
    for doc in confirmations_cursor:
        # Convert ObjectId to string for JSON serialization
        if "_id" in doc:
            doc["_id"] = str(doc["_id"])
        confirmations_list.append(doc)

    return confirmations_list

    return confirmations_query_result
