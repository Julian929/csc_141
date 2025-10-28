def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_info = build_profile('julian', 'lucas', location = 'reading', language = 'python', mood = 'happy')
print(user_info)