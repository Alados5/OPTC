import skillup

k = eval(input("Enter the number of skillups you need: "))
x = eval(input("Enter the minimum probability of getting those skillups you want (recommended around 0.7): "))

while True:
    event = input("Calculate with Skillup Chance x2? True/False: ")

    if event != "True" and event != "False":
        print("That's not right! Enter True or False \n")

    else:
        if event == "True":
            event = True
            break
        else:
            event = False
            break

print("\n")
print("The minimum number of copies you will need to level up a special",k,"times with a probability of at least",x,"is:")

nOC = skillup.NOC(k, x, event)
nMY = skillup.N(k, x, event)

print(nMY,"copies  -  with 1/10 normal (1/5 in x2) chance")
print(nOC,"copies  -  with 1/8 normal (1/4 in x2) chance")
