print('Give me two numbers ,and I will divide them .')
print('Enter q to quit.')

while True:
    first_number = input("\nfirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nsecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide a number by zero !")
    else:
        print(answer)