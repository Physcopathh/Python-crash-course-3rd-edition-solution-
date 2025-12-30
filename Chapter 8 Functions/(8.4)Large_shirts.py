def t_shits(size='large', message='I love python'):
    print(f'\nWe are printing "{message}" on to your {size} sized shirt\n')

t_shits(14,'helloworld')
t_shits(size=14,message='helloworld')
t_shits()
t_shits('medium')
t_shits(message='I dont love python')