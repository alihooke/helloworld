def challenge_1():
    first=input("What is your favorite food?")
    second=input("what is your favorite food?")
    print(first + second)

def challenge_2():
    total = int(input("What is the bill total?"))
    fifteen = total*.15
    twenty = total*.20
    print("Fifteen percent is %s" % fifteen)
    print("Twenty percent is %s" % twenty)

def challenge_2_2():
    total = int(input("What is the bill total?"))
    for i in range(1,100):
        tip = total*(i/100)
        print(i, "percent is {0:.2}".format(tip))

def challenge_3():
    price = int(input("What is the price of the car?"))
    tax = price*.10
    license = price*.01
    prep = 1000
    destination = 2300
    total = price + tax + license + prep + destination
    print(total)

challenge_3()