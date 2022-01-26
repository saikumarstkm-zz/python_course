started = False
stopped = True
while True:
    user_input = input('>').upper()
    if user_input == 'HELP':
        print('''Start - to start the car
Stop - to stop the car
quit - to exit''')
    elif user_input == 'START':
        if started:
            print('Car is already started.')
        else:
            print('Car started ...Ready to go..!!!')
            started = True
            stopped = False
    elif user_input == 'STOP':
        if stopped:
            print('Car is already stopped')
        else:
            print('Car stopped.')
            stopped = True
            started = False
    elif user_input == 'QUIT':
        print('Exiting now.')
        break
    else:
        print('Incorrect option selected . Please type help for more info.')
