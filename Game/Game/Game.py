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
            print('Text your mom(1)               Walk(2)')
            try:
                choice = int(input('Your Answer: '))
                if choice < 1.1:
                    print('When you text your mom she tells you how she is working and ')
                    print("to ask you'r dad to bring you home")
                    
                else:
                    print("As soon as you decide to walk home you see your friend's truck speeding away from the highschool  ")
                    print('but he had just texted you that he was at a dentist apointment???')
                    print(pause())
                    print('You decide to track him via SnapMap and follow him')

            except ValueError:
                print("")
                print('Thats not an option')
                exit()
        else:
            exit()

except ValueError:
        print("")
        print('Thats not an option')
        exit()