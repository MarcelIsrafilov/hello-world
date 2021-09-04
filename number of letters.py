sentence = input("Give a sentence to count the letters in: ")   #ask for a sentence
list_zin = []
for i in sentence:
    list_zin.append(i.lower())                                          #make a list of the sentence and make it all lowercase

number_of_letters = []                                          #add a list to count all the characters

for i in range(97, 123):
    number_of_letters.append((list_zin.count(chr(i)), chr(i)))  #count all the characters a-z

number_of_letters.sort(reverse=True)                            #sort the list in descending order of amount of letters
print("This is the number of each letter in the sentence: ")
for i in number_of_letters:
    print(i[1]+ ": " + str(i[0]))
