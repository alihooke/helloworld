__author__ = 'alihooke'
"""
giraffe
cow
dog
cat
snake
rat
hamster
horse
"""

def ask(question):
    x = input(question + "? ")
    return x == "yes"


def answer(x):
    print(x)
    exit()


if ask("Is it domestic"):
    if ask("is it a rodent"):
        if ask("does it have a long tail"):
            answer("rat")
        else:
            answer("hamster")
    else:
        if ask("does it meow"):
            answer("cat")
        else:
            answer("dog")
else:
    if ask("is it a farm animal"):
        if ask("does it neigh"):
            answer("horse")
        else:
            answer("cow")
    else:
        if ask("does it have legs"):
            answer("giraffe")
        else:
            answer("snake")