import string
import random

def genereer():
    wachtwoord = ""
    mogelijkheid = 0
    lengte = int(input("Wat moet de lengte van het wachtwoord worden?"))
    hoofdletter = input("Wil je hoofdletters in je wachtwoord? (voer ja of nee in!)")
    if hoofdletter.lower() == "ja":
        hoofdletter = True
    else:
        hoofdletter = False
    cijfers = input("Wil een cijfers in je wachtwoord? (voer ja of nee in!)")
    if cijfers.lower() == "ja":
        cijfers = True
    else:
        cijfers = False
    symbolen = input("Wil een speciale tekens in je wachtwoord? (voer ja of nee in!)")
    if symbolen.lower() == "ja":
        symbolen = True
    else:
        symbolen = False

    if hoofdletter == True and cijfers == True and symbolen == True:
        mogelijkheid = 1
    elif hoofdletter == True and cijfers == True and symbolen == False:
        mogelijkheid = 2
    elif hoofdletter == True and cijfers == False and symbolen == True:
        mogelijkheid = 3
    elif hoofdletter == False and cijfers == True and symbolen == True:
        mogelijkheid = 4
    elif hoofdletter == True and cijfers == False and symbolen == False:
        mogelijkheid = 5
    elif hoofdletter == False and cijfers == True and symbolen == False:
        mogelijkheid = 6
    elif hoofdletter == False and cijfers == False and symbolen == True:
        mogelijkheid = 7
    elif hoofdletter == False and cijfers == False and symbolen == False:
        mogelijkheid = 8
    else:
        print("Er is een foute combinatie ingevoerd.")
    for i in range(0, lengte):
        if mogelijkheid == 1:
            keuzelijst = str(string.punctuation) + str(string.ascii_letters) + str(string.digits)
            randomlijst = random.choice(keuzelijst)
            wachtwoord = wachtwoord + str(randomlijst)
        elif mogelijkheid == 2:
            keuzelijst = str(string.ascii_letters) + str(string.digits)
            randomlijst = random.choice(keuzelijst)
            wachtwoord = wachtwoord + str(randomlijst)
        elif mogelijkheid == 3:
            keuzelijst = str(string.punctuation) + str(string.ascii_letters)
            randomlijst = random.choice(keuzelijst)
            wachtwoord = wachtwoord + str(randomlijst)
        elif mogelijkheid == 4:
            keuzelijst = str(string.punctuation) + str(string.ascii_lowercase) + str(string.digits)
            randomlijst = random.choice(keuzelijst)
            wachtwoord = wachtwoord + str(randomlijst)
        elif mogelijkheid == 5:
            wachtwoord = wachtwoord + random.choice(string.ascii_letters)
        elif mogelijkheid == 6:
            keuzelijst = str(string.digits) + str(string.ascii_lowercase)
            randomlijst = random.choice(keuzelijst)
            wachtwoord = wachtwoord + str(randomlijst)
        elif mogelijkheid == 7:
            keuzelijst = str(string.punctuation) + str(string.ascii_lowercase)
            randomlijst = random.choice(keuzelijst)
            wachtwoord = wachtwoord + str(randomlijst)
        elif mogelijkheid == 8:
            wachtwoord = wachtwoord + random.choice(string.ascii_lowercase)
        else:
            wachtwoord = ""
    print(wachtwoord)

genereer();
