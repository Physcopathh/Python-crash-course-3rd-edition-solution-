#From achieve.py

msg = ['Hiiii sarah', 'Hello my brother', 'How you doing coder']
sent_msg = []

def sent_message(message):
    while True:
        messages = message.pop(0)
        print(messages)
        sent_msg.append(messages)
        if len(message) == 0:
            break

sent_message(msg[:])
print(msg)
print(sent_msg)



#Sending_message.py
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


#From cities.py
def city_name(city, country):
    x = '---------------------------------------------------------------------------------------'
    return f'{x}\n\t\t\t\t    {city}, {country}\n{x}'

print(city_name('Hyd', 'Pak'))