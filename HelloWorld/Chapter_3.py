__author__ = 'alexishooke'

def challenge_1():

    import random
    fortune = random.randint(1,5)
    if fortune == 1:
        print("Something you lost will soon turn up.")
    if fortune == 2:
        print("You will be invited to an exciting event.")
    if fortune == 3:
        print("The one you love is closer than you think.")
    if fortune == 4:
        print("Sun always shines after a downpour.")
    if fortune == 5:
        print("Idleness is the holiday of fools.")


def challenge_1_2():
    import random
    fortunelist=["Something you lost will soon turn up.","You will be invited to an exciting event.","You will be invited to an exciting event.","The one you love is closer than you think.","Sun always shines after a downpour.","Idleness is the holiday of fools."]
    fortune = random.choice(fortunelist)
    print(fortune)


def challenge_2():
    import random
    heads = tails = 0

    flips = int(input("How many times shall I flip a coin?"))
    while flips > heads+tails:
        coinflip = random.randint(0,1)
        if coinflip == 0:
            heads = heads + 1
        elif coinflip == 1:
            tails = tails + 1
        else:
            print("error")
    print("There were", heads, "heads and", tails, "tails.")

def challenge_3():
    import random
    number = random.randint(1,100)

    print("Welcome to Guess My Number")
    print("I'm thinking of a number between 1 and 100, try to guess it in as few attempts as possible")
    for attempt in range(5):
        guess = int(input("Take a guess: "))
        if guess != number:
            print("Lower" if guess > number else "Higher")
        else:
            print("Got it!")
            return
    print("you lose!")

def challenge_4():
    upper_bound = 100
    lower_bound = 0
    print("Think of a number between 1 and 100")
    response = "not correct"
    while response != "correct":
        guess = (upper_bound - lower_bound)//2 + lower_bound
        response = input("Is the number lower or higher than %s? If it is correct, write correct" % str(guess))
        if response == "higher":
            lower_bound = guess + 1
        elif response == "lower":
            upper_bound = guess - 1
    print("Yay!")

challenge_4()