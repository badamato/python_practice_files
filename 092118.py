##S-T-R-I-N-G-S

##UPPER
# string = 'this is my string'
# print(string.upper())

##CAPITALIZE
# string = 'this is my string'
# string = string.split()

# for i in string:
#     print(i[0].upper() + i[1:])

##REVERSED - looked this up, tried not to use reversed()
# string = 'this is my string'
# new_string = ''

# for i in string:
#     new_string = i + new_string
#     print(new_string)

##LEETSPEAK - without using .replace()
# phrase = input('Give me a phrase: ')
# uppercased_phrase = phrase.upper()
# converted = ''

# letter = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
# number = [4, 3, 6, 1, 0, 5, 7]

# for i in uppercased_phrase:
#     count = 0
#     translated_letter = ''
#     for j in letter:
#         if i == j:
#             translated_letter = str(number[count])
#             break
#         else:
#             translated_letter = i
#         count += 1
#     converted = converted + translated_letter
#     print(converted)

##LONG VOWELS
# vowels = 'aeiou'
# string = input('Enter a phrase: ')

##CAESAR
# string = 'lbh zhfg hayrnea jung lbh unir yrnearq'



##L-I-S-T-S

#sum
# nums = sum([1, 2, 3, 4])
# print(nums)

#largest
# nums = max([1, 2, 3, 4])
# print(nums)

#smallest
# nums = min([1, 2, 3, 4])
# print(nums)

#even
# nums = [0, 5, -44, 200, 2, 65]

# for x in nums:
#     if x % 2 == 0:
#         print(x)

#positive
# nums = [0, 5, -44, 200, 2, 65]

# for x in nums:
#     if x > 0:
#         print(x)

#positive 2
# nums = [0, 5, -44, 200, 2, 65]
# new_nums = []

# for x in nums:
#     if x > 0:
#         new_nums.append(x)
#     print(new_nums)


#multiply list
# ????

#multiply vectors
# ????


#de-dup
seq = []
jumble = "123abcdabcd123xyz987"
for l in jumble:
    seq.append(l)

# Create a variable for a new sequence
new_seq = []
# Iterate through our sequence
for i in seq:
    # If the current letter is not in the sequence,
    # add it.
    if i not in new_seq:
        new_seq.append(i)
print(new_seq)

