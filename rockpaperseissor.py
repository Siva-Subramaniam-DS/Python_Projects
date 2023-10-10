import random
class rps:
    count=0

    def __init__(self):
        pass

        
    @classmethod
    def game(cls,user):
        
        number=['rock','paper','scissor']
        c_number=random.choice(['rock','paper','scissor'])
        print(f'computer chose: {c_number}')

        if user==c_number:
            print("No point!")
        elif(number == 'rock' and c_number == 'scissor') or (number == 'rock' and c_number == 'rock') or (user == 'rock' and c_number == 'paper'):
            cls.count +=1
            print("You win")
        elif(number == 'paper' and c_number == 'scissor') or (number == 'paper' and c_number == 'rock') or (user == 'paper' and c_number == 'paper'):
            cls.count +=1
            print("You win")
        elif(number == 'scissor' and c_number == 'scissor') or (number == 'scissor' and c_number == 'rock') or (user == 'scissor' and c_number == 'paper'):
            cls.count +=1
            print("You win")
        else:
            print("I win")
            
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
