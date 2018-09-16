##RPS Coding Challenge
# from random import randint

# print('Welcome to ROCK, PAPER, SCISSORS!')

# rand_num = randint(0, 2)
# if rand_num == 0:
#     computer = 'rock'
# elif rand_num == 1:
#     computer = 'paper'
# else:
#     computer = 'scissors'
# print(f'Computer plays {computer}!')


# player = input('Player, please choose: ').lower()
# if player == computer:
# 	print("It's a tie!")
# elif player == "rock":
# 	if computer == "scissors":
# 		print("player wins!")
# 	else:
# 		print("computer wins!")
# elif player == "paper":
# 	if computer == "rock":
# 		print("player wins!")
# 	else:
# 		print("computer wins!")
# elif player == "scissors":
# 	if computer == "paper":
# 		print("player wins!")
# 	else:
# 		print("computer wins!")	
# else:
# 	print("Please enter a valid move!")


# for x in range(1,10):
#     print(x)

# for x in 'bruce':
#     print(x)
#     print(x*10)

# for x in range(3, 33, 1):
#     print(x)

# x = input('How many times do I have to tell you? ')
# x = int(x)
# for i in range(x):
#     print('CLEAN UP YOUR ROOM!')


# for i in range(1, 21):
#     if i % 2 == 0 and i != 4:
#         print(f'{i} is even')
#     elif i % 2 != 0 and i != 13:
#         print(f'{i} is odd')
#     elif i == 4 or i == 13:
#         print(f'{i} is unlucky')

########WHILE LOOPS
# star = '*'
# x = 1

# for x in range(1,11):
#     print(star * x)

# while x < 10:
#     print (star * x)
#     x = x + 1

### NESTED LOOP
# for x in range(2):
#     for x in range(1,11):
#         print('~' * x)

#EXERCISE
# response = input('How is it going? ')
# while response != 'stop copying me':
#     print(response)
#     response = input('')
# print('UGH FINE YOU WIN')


##USING BREAK
# while True:
#     msg = input('Type "exit" to exit: ')
#     if (msg == 'exit'):
#         break

# for x in range(0,31):
#     print(x)
#     if x == 3:
#         break


# x = int(input('How many times do I have to tell you? '))

# for i in range(x):
#     print('CLEAN UP YOUR ROOM!')
#     if i >= 5:
#         print('...do you even listen any more?!')
#         break


###GUESSING GAME CODE
# from random import randint
# i = randint(1,11)
# guess = int(input('Guess a number between 1 and 10: '))

# while guess != i:
#     if guess < i:
#         print('Too low, try again!')
#         guess = int(input('Guess a number between 1 and 10: '))
#     else:
#         print('Too high, try again!')
#         guess = int(input('Guess a number between 1 and 10: '))
# print('You guessed it!  YOU WON!')
# play = input('Do you want to keep playing? (y/n)  ')
# if play == 'y':
#     guess = int(input('Guess a number between 1 and 10: '))

#     while guess != i:
#         if guess < i:
#             print('Too low, try again!')
#             guess = int(input('Guess a number between 1 and 10: '))
#         else:
#             print('Too high, try again!')
#             guess = int(input('Guess a number between 1 and 10: '))
#     print('You guessed it!  YOU WON!')
#     play = input('Do you want to keep playing? (y/n)  ')
# else:
#     print('BYE - thanks for playing!')

##EXERCISE
# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# result = ('')

# for x in sounds:
#     result += x.upper()
#     print(result)

#or

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# print(''.join(sounds).upper())

##MORE WHILE LOOPS
# msg = input('Password: ')

# while msg != 'please':
#     print('guess again')
#     msg = input('Password: ')
# print('correct!')

# x = 0
# while x <= 50:
#     print(x)
#     x += 1 