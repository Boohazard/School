def wachtwoordchecker(wachtwoord):

    if len(wachtwoord) < 8:
        print("Wachtwoord is slecht.")
        return
    if hoodletter is True and str.isalpha(wachtwoord) is False:
        print("wachtwoord is sterk.")
        return

    print("Wachtwoord is matig.")


wachtwoord = input("Wat is je wachtwoord? ")
hoodletter = any(x.isupper() for x in wachtwoord)
wachtwoordchecker(wachtwoord)
