user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    delete_list = []
    for key, value in user_pref.items():
        if value == None or value == "":
            delete_list.append(key)
    for i in range(0, len(delete_list)):
        del user_pref[delete_list[i]]
    return user_pref


print(update_preferences(user_preferences))
