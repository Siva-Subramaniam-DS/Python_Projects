import random
class rps:
    count=0
    
    @classmethod
    def game(cls,user):
        user=user.lower()
        number=['rock','paper','scissor']
        c_number=random.choice(number)
        print(f'you choose : {user} ,computer chose: {c_number}')

        if user == c_number:
            print('its a tie')
            
        elif (user == 'rock' and c_number == 'scissor') or (user == 'scissor' and c_number == 'paper') or (user == 'paper' and c_number == 'rock'):
            cls.count +=1
            print("user win")
            
        else:
            print("computer win")
            
        print(f"so far your points: {cls.count}")

c1=rps()

while True:
        print()
        print("You want to play a game with me User (^_^)!!")
        print("Select the given number below:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissor")
        print("4. Check your points")


        user=int(input("Enter a Number: "))
    
        if user==1:
            c1.game("rock")
        elif user==2:
            c1.game("Paper")
        elif user==3:
            c1.game("Scissor")
        elif user==4:
            print(f"Total points: {rps.count}")
            print("Thank you for playing with me (^_-)!")
            break
