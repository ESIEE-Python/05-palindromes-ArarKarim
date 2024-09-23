#### Fonction secondaire

"""
main.py : Script principal
"""


def ispalindrome(p):
    """
    Vérifie si la chaîne donnée est un palindrome.
    """
    accent = str.maketrans( "àáâäèéêëìíîïòóôöùúûüÀÁÂÄÈÉÊËÌÍÎÏÒÓÔÖÙÚÛÜçÇ",
        "aaaaeeeeiiiioooouuuuAAAAEEEEIIIIOOOOUUUUcC")
    p = p.translate(accent)
    p = ''.join(char.lower() for char in p if char.isalnum())
    if p == p[::-1]:
        return True
    return False

#### Fonction principale


def main():
    """
    Fonction principale pour tester la fonction ispalindrome avec différentes chaînes.
    """

    print(ispalindrome("bob"))
    print(ispalindrome("salut"))
    print(ispalindrome("Tu l'as trop écrasé, César, ce port-salut "))
    print(ispalindrome("Madame"))
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
