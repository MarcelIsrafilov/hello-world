sentence = input("Give a sentence to count the letters in: ")           #ask for a sentence
list_sentence = []
for i in sentence:
    list_sentence.append(i.lower())                                     #make a list of the sentence and make it all lowercase

number_of_letters = []                                                  #add a list to count all the characters

for i in range(97, 123):
    number_of_letters.append((list_sentence.count(chr(i)), chr(i)))     #count all the characters a-z

number_of_letters.sort(reverse=True)                                    #sort the list in descending order of amount of letters
print("This is the number of each letter in the sentence: ")
all_occur = True                                                        #adding a variable which checks whether all letters of the alphabet were found
for i in number_of_letters:                                             #printing the number of letters
    if i[0]>0:
        print(i[1]+ ": " + str(i[0]))
    else:
        all_occur = False

if not all_occur:                                                       #says whether or not all letters occured
    print("The rest of the letter(s) didn't occur in the sentence")
