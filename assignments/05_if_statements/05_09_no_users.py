usernames = ['Admin', 'Julian', 'Eren', 'Braden', 'Jude']
if usernames:
    for username in usernames:
       if username == 'Admin':
          print(f"Hello {username}, would you like to see a status report?")
       else:
          print(f"Hello {username}. thank you for logging in again.")   
else:
   print("We need to fins some users!")

usernames = []
if usernames:
    for username in usernames:
       if username == 'Admin':
          print(f"Hello {username}, would you like to see a status report?")
       else:
          print(f"Hello {username}. thank you for logging in again.")   
else:
   print(f"We need to find some users!")