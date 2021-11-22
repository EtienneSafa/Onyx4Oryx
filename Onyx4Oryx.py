
# Features' status last checkup date
#   check list: 
#   - nb of keystrokes in macros
date = '2020-11-19'



from time import sleep as sleep
import gui.py





def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        return("INT")
    except ValueError:
        return("STR")





f = open('layouts.txt','r', encoding="utf-8")




# Fetch layouts in layouts.txt using "||" as a separator
layouts = {}

for line in f:
    Line = line.split('\n')[0]
    layouts[Line.split('=',1)[0]] = Line.split('=',1)[1].split('||')

knownLayouts = list(layouts.keys())
knownLayouts.remove('English (qwerty)')
knownLayouts.sort()




# Inquire for user choice
print ("\n   (⌐■_■)  >>  Onyx4Oryx will translate the keys you need for your macros if you're working on a non-qwerty keyboard.\n           >>  Here are the layouts currently available at development stage:\n")


while True:
    for layout in knownLayouts:
        print(f"          [{knownLayouts.index(layout)}]  {layout}")


    sleep(1)

    choice = input("\n\n ╰(*°▽°*)╯ >>  Which layout wou'd you like to translate?\n\n       you >>  ")


    while True:
        if check_user_input(choice) == "INT":
            choice = int(choice)
            if choice in range(0,len(knownLayouts)-1):
                break
            else:
                choice = (input("\n\n  '￣へ￣  >>  That's not in the list...\n\n       you >>  "))
                pass
        else:
            choice = (input("\n\n o(≧口≦)o  >>  That's not a number...\n\n       you >>  "))
            pass

    usrLayout=knownLayouts[choice]



    while True:
        sequence = input(f"\n   (⌐■_■)  >>  OK for \"{usrLayout}\". Please enter your sequence (only simple keystrokes: don't use any modifiers as you'll be able to tick them on Oryx)\n\n       you >>  ")

        while True:
            if len(sequence) > 5:
                sequence = input(f"\nㄟ( ▔, ▔ )ㄏ >> Oryx can only take 5 keystrokes as of now ({date})\n\n       you >>  ")
            else:
                break

        S = list(sequence)

        sleep(0.33)

        print("\n\n (￣y▽￣)╭ >>  Here it is!")


        for letter in S:
        #    idx = sequence.find(letter)
            for row in layouts[usrLayout]:
                rowIdx = layouts[usrLayout].index(row)
                if row.find(letter) != -1:
                    row = list(layouts[usrLayout][rowIdx])
                    ltrIdx = row.index(letter)
                    l = list(layouts['English (qwerty)'][rowIdx])
                    print('       ', letter, '-->', l[ltrIdx])
        
    
        sleep(3)


        repeat = input('\n\n   (⌐■_■)  >>  Would you like to input a new sequence? (Yes/No)\n           >>  You can also change the layout by typing "change layout" (don\'t make any typos...)\n\n       you >>  ')
        
        if repeat in ['yes', 'Yes', 'y', 'Y', 'YES']:
            pass
        elif repeat in ['no','No','n','N','NO','q','Q','quit']:
            print("\n\nSee ya'!  ¯\_(ツ)_/¯\n\n")
            break
        elif repeat in ["change layout", "Change layout"]:
            break
        else:
            print ('\n   (⌐■_■)  >>  What was that?')
            pass
    
    if repeat in ["change layout", "Change layout"]:
        pass
    else:
        break