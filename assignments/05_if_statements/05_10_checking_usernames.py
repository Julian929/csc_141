current_users = ['Admin', 'Julian', 'Eren', 'Braden', 'Jude']

new_users = ['Vince', 'Dante', 'Drew', 'JSean', 'jude']

for new_user in new_users:
    if new_user.upper() in current_users:
        print("This username is already in use. Please select another.")
    else:
        print("This username is available.")