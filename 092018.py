## September 19

##day of the week
# day = int(input('Day (0-6)? '))
# dow = ''

# if day == 0:
#     dow = 'Sunday'
# if day == 1:
#     dow = 'Monday'
# if day == 2:
#     dow = 'Tuesday'
# if day == 3:
#     dow = 'Wednesday'
# if day == 4:
#     dow = 'Thursday'
# if day == 5:
#     dow = 'Friday'
# if day == 6:
#     dow = 'Saturday'
# print(dow)



##WORK OR SLEEP IN
# day = int(input('Day (0-6)? '))
# option = ''

# if day == 0:
#     option = 'Sleep in'
# elif day == 1:
#     option = 'Go to work'
# elif day == 2:
#     option = 'Go to work'
# elif day == 3:
#     option = 'Go to work'
# elif day == 4:
#     option = 'Go to work'
# elif day == 5:
#     option = 'Go to work'
# else:
#     option = 'Sleep in'
# print(option)


##C to F
# ctemp = int(input('Temperature in C? '))
# ftemp = (ctemp * 1.8) + 32
# print(ftemp)


##TIP CALC
# bill_total = float(input('Total bill amount: '))
# service = input('Good, fair, or bad service: ')

# good = .20
# fair = .15
# bad = .10

# if service == 'good':
#     tip_amount = bill_total * good
#     total = bill_total + tip_amount
# elif service == 'fair':
#     tip_amount = bill_total * fair
#     total = bill_total + tip_amount
# else:
#     tip_amount = bill_total * bad
#     total = bill_total + tip_amount
    
# print('Tip amount: %.2f' % tip_amount)
# print('Total amount: %.2f' % total)



##TIP CALC 2
# bill_total = float(input('Total bill amount: '))
# service = input('Good, fair, or bad service: ')
# split = int(input('Split how many ways: '))

# good = .20
# fair = .15
# bad = .10

# if service == 'good':
#     tip_amount = bill_total * good
#     total = bill_total + tip_amount
#     divided = total / split
# elif service == 'fair':
#     tip_amount = bill_total * fair
#     total = bill_total + tip_amount
#     divided = total / split
# else:
#     tip_amount = bill_total * bad
#     total = bill_total + tip_amount
#     divided = total / split
    
# print('Tip amount: %.2f' % tip_amount)
# print('Total amount: %.2f' % total)
# print('Amount per person: %.2f' % divided)







##1 to 10 while loop
# num = 0
# while num <= 10:
#     print(num)
#     num += 1

##NtoM while loop
# n = int(input('Starting number (bet 0-100): '))
# m = int(input('Ending number (bet 0-100): '))
# x = n
# while x <= m:
#     print(x)
#     x += 1


##PRINT ODDS
# for i in range(11):
#     if i % 2 != 0:
#         print(i)

##COINS
# 

##5x5 square
# star = '*'
# num = 5

# for x in range(num):
#     for y in range(num):
#         print(star, end=' ')
#     print()

##NbyN square
# star = '*'
# num = int(input('How big is the square: '))

# for x in range(num):
#     for y in range(num):
#         print(star, end=' ')
#     print()

##HOLLOW BOX
# n = int(input('Number of rows/columns: '))
# emoji = ('\U0001f601')

# for row in range(n): # rows
#     for col in range(n):  #column top
#         if row == 0 or row == (n-1) or col == 0 or col == (n-1):  # column middle
#             print(emoji + " ", end='')
#         else: 
#             print('  ', end="")
#     print()

##TRIANGLE 1
# num = int(input('Enter number of rows: '))
# emoji = ('\U0001f601')

# for i in range(0, num): #rows
#     for j in range(0, num - i - 1): #columns
#         print(end = ' ')
#     for j in range(0, i + 1):
#         print(emoji, end = ' ')
#     print()


##MULTIPLICATION TABLE
# for x in range(1, 11):
#     for y in range(1, 11):
#         print("%d x %d = %d" % (x, y, (x * y)))



##BANNER
# text = input('Banner slogan: ')
# star = ''

# for i in range(len(text) + 4):
#     star = star + '*'

#     print(star)
#     print('* %s *' % text)
#     print(star)