def palin(word):
    print("Słowo jest palindromem")
    return(word==word[::-1])
print(palin("kodilla"))
print(palin("kajak"))