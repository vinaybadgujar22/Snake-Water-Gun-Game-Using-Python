#Snake Water Gun Game
import random


def winnerround(plr1,cpu1):
    global plr1_name
    global cpu1_nane
    if (plr1 == "W" and cpu1 == "S") or (plr1=="G" and cpu1=="W") or (plr1=="S" and cpu1=="G"):
        result= f"Winner of this round is {cpu1_nane}"
        return result


    elif (cpu1 == "W" and plr1 == "S") or (cpu1=="G" and plr1=="W") or (cpu1=="S" and plr1=="G"):
        result= f"Winner of this round is {plr1_name}"
        return result
    else:
        result = f"NO one is winner"
        return result






print("\n\t\t\t---Welcome to Snake-Water-Gun Game---\n")

plr1_name = input("Enter Your Name: ")
cpu1_nane = "Computer"
plr1_Score = 0
computer_Score = 0

rounds = int(input(f"\nSelect number of rounds you want to play against Computer {plr1_name} (e.g:1,2,3...):\n"))
lst = ["S","W","G"]
i = 0
while i<rounds:
    print("Snake,Water,Gun")
    print("Choose\nS-for Snake\nW-Water\nG-Gun\n")
    u = input(f"Enter your Choice {plr1_name} :\n")
    plr1_Choice = u.upper()

    if plr1_Choice=="S" or plr1_Choice=="W" or plr1_Choice=="G":
        cpu1_chaice = random.choice(lst)
        print(cpu1_chaice)

        g = winnerround(plr1_Choice,cpu1_chaice)
        print(g)

        if g == f"Winner of this round is {plr1_name}":
            plr1_Score +=1
        elif g == f"Winner of this round is {cpu1_nane}":
            computer_Score +=1
    else:
        print(f"Enter Valid Choice {plr1_name}")

    i = i + 1
    print(f"Number of round left is {rounds - i}\n\n")
    if i==rounds:
        print(f"\n{plr1_name}'s Overall Score is{plr1_Score}")
        print(f"{cpu1_nane}'s Overall Score is{computer_Score}\n\n")
        if plr1_Score < computer_Score:
            print(f"\t\tWinner of thie Snake-Water-Gun Game is {cpu1_nane}!")
        elif plr1_Score > computer_Score:
            print(f"\t\tWinner of this Snake-Water-Gun Game is {plr1_name}!")
        else:
            print("It's a Tie Game!")




