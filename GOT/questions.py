from got import characters  #from the got.py file import the characters dictionary

#How many characters names start with "A"?
def how_many(letter):
    count = 0
    for person in characters:
        if person['name'] != ''and person['name'][0] == letter:
            count = count + 1

    # print(count)
    return(count)


#How many characters names start with "Z"?
starts_with_a = how_many('Z')
print(starts_with_a)

#How many characters are dead?
##no arguements needed here because nothing needs to passed in that will continually change
def many_dead():
    count = 0
    for person in characters:
        if person['died'] != '':
            count = count + 1
    return count

dead_count = many_dead()
print('%d are dead' % dead_count)

#Who has the most titles?
title_lenths = []
for person in characters:
    #get the length of the 'titles' key
    num_titles = len(person['titles'])
    title_lenths.append(num_titles)

record_for_most_titles = max(title_lenths)
print(record_for_most_titles)

index_of_record = title_lenths.index(record_for_most_titles)
# print(index_of_record)
person_with_title_record = characters[index_of_record]
print(person_with_title_record['name'])

#How many are Valyrian?

#What actor plays "Hot Pie" (and don't use IMDB)?
for person in characters:
    if person['name'] == 'Hot Pie':
        print(person['playedBy'][0])

#How many characters are *not* in the tv show?
#Produce a list characters with the last name "Targaryen"
def find_last-name:
    count = 0
    for person in characters:
        if person['lastname'] == 

#Create a histogram of the houses (it's the "allegiances" key)