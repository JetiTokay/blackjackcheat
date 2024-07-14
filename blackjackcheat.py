#this is a balckjack cheat sheet , how to use the app, asked you a question "what are you cards". you replied your cards and it will
#let you know what to do next based on simple stradgy 


print('what are your cards?: ')
cards = input()

#pairs 

if (cards == 'AA', 'aa'):
    print ('Always Split Aces') 
if (cards == '1010'):
    print('Never Split 10')
if (cards == '99'):
    print('Split against dealer 2-9 ,expt for 7,otherwise STAND')
if (cards == '88'):
    print('Always split 88')
if (cards == '44'):
    print('Split against dealer 5 & 6, otherwise hit')
if (cards == '22'):
    print('Split against dealer 2-7, otherwse hit')

#surrenders
if (cards == '16'):
    print('Surrender against 9-A')
if (cards == '15'):
    print('surrender against 10')
if (cards == '17', '18', '19', '20', '21'):
    print('STAND')
if (cards == '13', '14', '15', '16'):
    print('Stand against 2-6, HIT against 7-Ace')
if (cards == '12'):
    print('Stand against 4-6, HIT against everything else ')
if (cards == '11'):
    print('Double Down')
if (cards == '10'):
    print('Double against 2-9') 
if (cards == '9'):
    print('Double against 3-6')
if (cards <= '8'):
    print('Hit')

elif (cards <= 0):
    print('try again')

#SOFT HANDS 
    

    









    








