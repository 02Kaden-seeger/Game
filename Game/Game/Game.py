'''
Kaden Seeger
4.17.19
Game
'''
print('')
print('')
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
                    print(pause())
                    print('when you ask your dad he tells you he will be there in 30 minutes')
                    print('he also tells you to wait at the library near by to get homework done')
                    print(pause())
                else:
                    print("As soon as you decide to walk home you see your friend's truck speeding away from the highschool  ")
                    print('but he had just texted you that he was at a dentist apointment???')
                    print(pause())
                    print('You decide to track him via SnapMap and follow him')
                    print(pause())
                    print("when you follow him you see he is stopped at a location you don't recognize")
                    print('when you get to the location you see it is an abandoned warehouse  ')
                    print("Do you go in the warehouse or do you text you'r friend")
                    print("Go in the warehouse(1)            text you'r friend(2)")
                    try:
                        choice = int(input('Your Answer: '))
                        if choice < 1.1:
                            print('When you go into the warehouse you can see that the company that owns this building is the same one')
                            print("that you'r friend's dad owns")
                            print(pause())
                            print('When you go through some doors you are in a room that has two doors one on the right and one on the left')
                            print('which one do you take?')
                            print('Right(1)                Left(2)')
                        else:
                            print('when you text your friend and asks him what he is doing in a warehouse he ')
                            print('said to come in through the garage and find out')
                            print(pause())
                            print('you then realize that there are people watching you from the road with black hoods and pitchforks ')
                            print(pause())
                            print("so you go inside through the garage because you dont want to mess with them")
                            print(pause())
                            print('when you go through the garage door you can see how massive the garage inside it is')
                            print('the warehouse must have been an automotive storage warehouse')
                            print(pause())
                            print('')
                    except ValueError:
                        print("")
                        print('Thats not an option')
                        exit()
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