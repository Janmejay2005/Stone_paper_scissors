import random

print("For cutter say (S)\nFor paper say (P)\nFor Stone say (R)")

a = input("Enter your guess: ").upper()

choices = ['R', 'P', 'S']
Your_choice = random.choice(choices)

print(f"Computer chose: {Your_choice}")

if a == Your_choice:
    print("It's a tie!")
elif (a == 'R' and Your_choice == 'S') or (a == 'P' and Your_choice == 'R') or (a == 'S' and Your_choice == 'P'):
    print("You win!")
else:
    print("You lose!")

