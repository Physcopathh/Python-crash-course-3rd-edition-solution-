prompt = 'Tell me what topping you like'
prompt += '\n enter\'quit\' to stop: '
topping = input(prompt)

while topping != 'quit':
    print(f'\nadding {topping} to your pizza\n')
    topping = input(prompt)