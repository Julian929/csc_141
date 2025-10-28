def show_messages(messages):
    """Print text messages."""
    for message in messages:
        print(message)

# show_messages(messages)

def send_messages(message, sent_messages):
    """Print messages and move to list"""
    while send_messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

messages = ['Hi', ';How are you?', 'Hello there!']
send_messages = []

send_messages(messages, sent_messages)
print(messages)
print(sent_messages)
