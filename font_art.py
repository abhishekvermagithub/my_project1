print('*** Welcome to Our Font Art Creater ***\n')          #Project title

import pyfiglet
while True:
    name = input('Enter your name (or q/Q to Quit): ')      # Input text/name or Exit
    if name.lower() == 'q':      
        print('Thank you, See you again!')
        break
    
    print('''\nHere are some font styles available for you:      
    standard                                                
    digital
    doom
    epic
    slant
    banner
    big
    block
    isometric1
    roman
    larry3d
    bubble
    bulbhead
    shadow''')

    font = input('\nChoose any given font style: ')           # Input font style
    create = pyfiglet.figlet_format(name, font)             # Font art function
    print(create)