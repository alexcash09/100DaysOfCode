while True:
    try:
        x = int(input('Please input number:'))
        break
    except ValueError:
        print('that was not a number')

        
