import pandas as pd

PHONETICS = {
    "letters" : ["A","B","C","D","E",
             "F","G","H","I","J","K","L","M","N","O",
             "P","Q","R","S", "T","U","V","W", "X","Y","Z"],
    "phonetics" : ["Alpha","Beta","Charlie","Delta","Echo",
             "Foxtrot","Golf","Hotel","India","Juliet",
             "Kilo","Lima","Mike","November","Oscar",
             "Papa","Quebec","Romeo","Sierra",
             "Tango","Uniform","Victor","Whiskey",
             "X-Ray","Yankee","Zulu"]
}

phonetic_dataframe = pd.DataFrame(PHONETICS)

game_on = True
while game_on == True:
    full_word = input("Enter Word: ")
    phonetic_list = [PHONETICS["phonetics"][PHONETICS["letters"].index(letter.upper())] for letter in full_word]
    print(phonetic_list)
    if full_word == "exit":
        game_on = False

#for letter in word:
    