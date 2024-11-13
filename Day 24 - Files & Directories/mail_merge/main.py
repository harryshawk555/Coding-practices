#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PATH_LETTER = r"Day 24 - Files & Directories/mail_merge/Input/Letters/starting_letter.txt"
PATH_NAMES = r"Day 24 - Files & Directories/mail_merge/Input/Names/invited_names.txt"
PATH_OUT = r"Day 24 - Files & Directories/mail_merge/Output/ReadyToSend/"
REPLACE = "[name]"

def open_letter():
    with open(PATH_LETTER,"r") as file:
        file.read
        letter =  file.readlines()
    return letter

with open(PATH_NAMES,"r") as file:
    file.read
    names = file.readlines()


for i in range(len(names)):
    file = open((f"{PATH_OUT}{names[i][:-1]}_letter.txt"),"w")
    out_letter = open_letter()
    out_str = ""
    for j in range(len(out_letter)):
        if out_letter[j].find(REPLACE):
            out_letter[j] = out_letter[j].replace(REPLACE,names[i])
    for j in out_letter:
        out_str += f"{j}"
    file.write(out_str)
    file.close()
