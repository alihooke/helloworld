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

def challenge_2():
    import random
    coinflip = random.randint(1, 2)
    if coinflip() == 1:
        print("heads")
    if coinflip() == 2:
        print("tails")


def challenge_1_2():
    import random
    fortunelist=["Something you lost will soon turn up.","You will be invited to an exciting event.","You will be invited to an exciting event.","The one you love is closer than you think.","Sun always shines after a downpour.","Idleness is the holiday of fools."]
    fortune = random.choice(fortunelist)
    print(fortune)

challenge_1_2()




