'''
Kaden Seeger
4.17.19
Game
'''
print ('Hello and welcome to my game ')
print ('My name is Kaden Seeger')
print('')
print ('When there is no text try pressing enter')
def pause():
    
   choice = input('')

print (pause())
print('Good Job!')
print('In this game you will be given choices like this')
print('Do you understand?')
print('yes(1)           no(2)')
try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print('Ok now into the game')
            print(pause())
            print('You are just walking out of highschool and you get a text  ')
            print('it is your best friend, he tells you how he had to leave early for a dentist apointment ')
            print("How will you get home?! He was you'r ride!")
            try:
                choice = int(input('Your Answer: '))
                if choice < 1.1:
                    print('ride(1)')

                else

            except ValueError:
                print("")
        print('Thats not an option')
        exit()
            print('')
        else:
            exit()

except ValueError:
        print("")
        print('Thats not an option')
        exit()