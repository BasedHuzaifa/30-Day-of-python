import random
user_number=input("Guess the number:")
number = random.randint(1,20)
if user_number == number:
    print("Correct Number, the number was:",number)
else:
    print("wrong number")