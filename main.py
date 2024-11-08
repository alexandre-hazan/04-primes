""" import de la fonction sqrt """
from math import sqrt


#### Fonction secondaire


def isprime(p):
    """methode qui renvoie True si le nombre est premier """
    if p==1:
        return False
    for i in range (2,(int)(sqrt(p)+1)):
        if p %i==0:
            return False
    return True


#### Fonction principale


def main():
    """main qui s'occupe de tester la fonction créée précedement """

    # vos appels à la fonction secondaire ici
    isprime(33)
    isprime(43)
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
