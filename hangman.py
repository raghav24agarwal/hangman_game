import random

l1 = ["pycharm","hyperloop","engineering","pacman","university","kingsman","resources","random","unnatural","fantastic","governor","comparison",
      "scattered","dispensable","redundant","barbarous","attraction","envious","symptomatic","tiresome","adaptable","mountain","insurance",
      "addition","vigorous","unknown","important","tasteless","discussion","downtown","violent","romantic","payment","calculator","impervious",
      "hallowed","unfasten","aberrant","gruesome","outrageous","efficacious","vivacious","parsimonious","acoustics","program","precious",
      "application","virtual","bottle","tractor","keyboard","telephone","difficult","character","document","folder","world","superman","avengers"]

print("Welcome")
print("Time to play Hangman")

def hang():

    word = random.choice(l1)
    flag = 0
    guess = {}
    k = 0

    for i in range(len(word)):
        guess[i] = "-"

    a = {}

    for i in range(len(word)):
        a[i] = word[i]

    turns = len(word) + 5


    #name = input("Enter your name")
    #print("Hello " + name )
    print("Guess the word"+"\n"+f"You have {turns} turns")

    for i in range(len(word)):
        print("-", end = '')
    print()


    while(turns>0):
        failed = 0
        char = input("Enter a character")
        char = char.lower()

        if char in word and len(char) == 1:
            for i in range(len(word)):
                if char == word[i]:
                    if guess[i] == char:
                        print("Same letter again")
                        turns = turns + 1
                    else:
                        guess[i] = char
                        k = k+1

        else:
            if(len(char) != 1):
                print("Length of character must be one")
                turns = turns+1
            else:
                print("Wrong guess")

            #failed = failed +1

        for i in range(len(guess)):
            print(guess[i], end = "")
        print()
        turns = turns - 1

        if k == len(word):
            print("you won")
            flag = 1
            break

        print("No of turns remaining ", turns)

    if flag == 0:
        print("You Lose")
        print(f"Correct Answer - {word}")

    choice = input("Want to play again?(Y/N)")
    if choice.upper() == "Y":
        hang()


hang()