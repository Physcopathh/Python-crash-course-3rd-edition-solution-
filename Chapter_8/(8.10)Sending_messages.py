msg = ['Hiiii sarah', 'Hello my brother', 'How you doing coder']
sent_msg = []
def sent_message(message):
    while True:
        messages = message.pop()
        print(messages)
        sent_msg.append(messages)
        if len(message) == 0:
            break

sent_message(msg)
print(msg)
print(sent_msg)