numbers = []
while len(numbers) < 10:
    number = input ('Input a number: ')
    if number == '':
        break
    elif not number.isdigit():
        print('It\'s not a number')
    else:
        numbers.append(int(number))

if len(numbers) != 0:
    print (sum (numbers) / len(numbers))

