import skillup

n = eval(input("Enter the number of copies you have: "))
k = eval(input("Enter the number of skillups you need: "))

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

while True:
    japan = input("Calculate with Japan Rates? True/False: ")

    if japan != "True" and japan != "False":
        print("That's not right! Enter True or False \n")

    else:
        if japan == "True":
            japan = True
            break
        else:
            japan = False
            break



print("\n")

if n == 1:
    if k == 1:
        print("With",n,"copy, the probability of leveling up the special",
              k,"time...")
    else:
        print("With",n,"copy, the probability of leveling up the special",
              k,"times...")
else:
    if k == 1:
        print("With",n,"copies, the probability of leveling up the special",
              k,"time...")
    else:
        print("With",n,"copies, the probability of leveling up the special",
              k,"times...")

probOC = skillup.LvOC(k, n, event, japan)
probOC = str(100*probOC)[:6]
probMY = skillup.Lv(k, n, event, japan)
probMY = str(100*probMY)[:6]

if japan:
    print("\t ...with JAPAN SKILLUP RATES and...")
    if event:
        print("\t ...'x2 chance' event ACTIVE is: \n")
        print(probMY,"%  \t- with 1/3 chance")
        print(probOC,"%  \t- with 2/5 chance")
    else:
        print("\t ...'x2 chance' event NOT active is: \n")
        print(probMY,"%  \t- with 1/6 chance")
        print(probOC,"%  \t- with 1/5 chance")

else:
    print("\t ...with GLOBAL SKILLUP RATES and...")
    if event:
        print("\t ...'x2 chance' event ACTIVE is: \n")
        print(probMY,"%  \t- with 1/5 chance")
        print(probOC,"%  \t- with 1/4 chance")
    else:
        print("\t ...'x2 chance' event NOT active is: \n")
        print(probMY,"%  \t- with 1/10 chance")
        print(probOC,"%  \t- with 1/8 chance")

print("\n")
