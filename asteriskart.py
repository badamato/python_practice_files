emoji = ('\U0001f601')

##LEFT ALIGNED TRIANGLE
# num = int(input("Enter a # between 1-10: "))

# for i in range(1, num + 1): #rows
#     for j in range(1, i + 1):  #columns
#         print(emoji, end=" ")
#     print()

##LEFT ALIGNED TRIANGLE WITH ENDS INCREASING BY TWO
# user_rows = int(input("Enter number of rows: "))
# k = 1

# for i in range(1, user_rows + 1): #rows
#     for j in range(1, k + 1): #columns
#         print(emoji, end=" ")
#     k = k + 2
#     print()


##SOLID TRIANGLE
# num = int(input("Enter number of rows: "))

# for i in range(0, num): #rows
#     for j in range(0, num - i - 1): #columns
#         print(end = " ")
#     for j in range(0, i + 1):
#         print(emoji, end = " ")
#     print()

##SOLID BOX
# num = int(input("Enter number of rows: "))

# for i in range(0, num): #rows
#     for j in range(0, num): #columns
#         print(emoji, end = " ")
#     print()


#FLOYDS TRIANGLE
# n = int(input("Enter number of rows: "))
# num = 1

# for row in range(1, n + 1):
#     for col in range(1, row + 1):
#         print(num, end = ' ')
#         num += 1
#     print() #prints new line


#PYRAMID made from a word
# string = input("Enter a word: ").lower()
# length = len(string)

# for row in range(length):  ##defining the rows
#     for col in range(row + 1):  ##defining the columns
#         print(string[col], end = '')
#     print() #prints new line


#HOLLOW BOX
# n = int(input('Number of rows/columns: '))

# for row in range(n): # rows
#     for col in range(n):  #column top
#         if row == 0 or row == (n-1) or col == 0 or col == (n-1):  # column middle
#             print(emoji, end='')
#         else: 
#             print(end=' ')
#     print()


##DIAMOND SHAPE - must use a function as there are two diamond patterns
# def pyramid(rows):
#     for i in range(rows): ##top of the diamond - top pyramid
#         print(' ' * (rows - i - 1) + '* ' * (i + 1))
#     for j in range(rows - 1, 0, -1): ##bottom of the diamond - after middle line
#         print(' ' * (rows - j) + '* ' * (j))

# pyramid(10)
