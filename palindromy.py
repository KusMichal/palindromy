def palin(word):
    if(word==word[::-1]):
        return "to słowo to palindrom"
    else:
        return "to słowo nie jest palindromem"
print(palin("ala"))
print(palin("Kodilla"))