while True:
    try:
        text = open(input("Give a file with its directory to count the lettetrs in: "))
        break
    except FileNotFoundError:
        print("This file wasn't found, please check for any mistakes in the name or directory")


readtext = text.read()                                                              
list_text = []
for i in readtext:
    list_text.append(i.lower())                                                     #make a list of the text and make it all lowercase

number_of_letters = []                                                              

for i in range(97, 123):
    number_of_letters.append((list_text.count(chr(i)), chr(i)))                     #count all the characters a-z

number_of_letters.sort(reverse=True)                                                #sort the list in descending order of amount of letters
print("This is the number of each letter in the sentence: ")
all_occur = True                                                                    #adding a variable which checks whether all letters of the alphabet were found
for i in number_of_letters:                                                         
    if i[0]>0:
        print(i[1]+ ": " + str(i[0]))
    else:
        all_occur = False

if not all_occur:                                                                   #says whether or not all letters occured
    print("The rest of the letter(s) didn't occur in the sentence")
