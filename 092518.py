##PHONEBOOK
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

#Print Elizabeth's phone number.
# print(phonebook_dict['Alice'])

#Add an entry to the dictionary: Kareem's number is 938-489-1234.
# phonebook_dict['Kareem'] = '938-489-1234'

#Delete Alice's phone entry.
# del phonebook_dict['Alice']

#Change Bob's phone number to '968-345-2345'.
# phonebook_dict['Bob'] = '968-345-2345'

#Print all the phone entries.
# for x, y in phonebook_dict.items():
#     print("%s: %s" % (x, y))

#or

for person in phonebook


##PHONEBOOK 2

# ramit = {
#     'name': 'Ramit',
#     'email': 'ramit@gmail.com',
#     'interests': ['movies', 'tennis'],
#     'friends': [
#     {
#         'name': 'Jasmine',
#         'email': 'jasmine@yahoo.com',
#         'interests': ['photography', 'tennis']
#     },
#     {
#         'name': 'Jan',
#         'email': 'jan@hotmail.com',
#         'interests': ['movies', 'tv']
#     }
#     ]
# }

# Write a python expression that gets the email address of Ramit.
# print(ramit['email'])

# Write a python expression that gets the first of Ramit's interests.
# print(ramit['interests'][0])

# Write a python expression that gets the email address of Jasmine.
# print(ramit['friends'][0]['email'])

# Write a python expression that gets the second of Jan's two interests.
# print(ramit['friends'][1]['interests'][1])

##LETTER SUMMARY - histogram
#Write a letter_histogram program that asks the user for input, and prints a
# dictionary containing the tally of how many times each letter in the 
# alphabet was used in the word. 

# Please enter a word: banana
# {'a': 3, 'b': 1, 'n': 2}

def letter_hist(word):
    letter_dictionary = {}
    