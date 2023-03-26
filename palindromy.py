def palin(word):
    print("Słowo jest palindromem")
    word = word.strip()
    word = word.lower()
    word = word.split()
    word = "".join(word)
    znaki = ("!",",",".","?","(",")",":",";","/","`","<",">","@","-","+")
    for a in word:
        if a in znaki:
            word = word.replace(a,"")
    return(word==word[::-1])
print(palin("kodilla   "))
print(palin("Kajak ,,..,. kajak!+---++    "))