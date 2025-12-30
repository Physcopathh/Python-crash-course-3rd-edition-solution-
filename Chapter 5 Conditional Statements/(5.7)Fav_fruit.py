fav_fruits = ['mango','dates','apple']
        
fruits = ['apple','banana','orange','aeroplane','mango','dates']
for f in fruits:
    if f in fav_fruits:
        print('You really like\n', f,'\n')
    else:
        print('Not a big fan of\n', f,'!\n')
        