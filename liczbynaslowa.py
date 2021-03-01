
jednosci = ["", "jeden ", "dwa ", "trzy ",
        "cztery ", "pięć ", "sześć ", "siedem ", "osiem ", "dziewięć " ]
dziesiatki = [ "", "dziesięć ", "dwadzieścia ",
        "trzydzieści ", "czterdzieści ", "pięćdziesiąt ",
        "sześćdziesiąt ", "siedemdziesiąt ", "osiemdziesiąt ",
        "dziewięćdziesiąt "]
nascie = ["dziesięć ", "jedenaście ", "dwanaście ",
        "trzynaście ", "czternaście ", "piętnaście ", "szesnaście ",
        "siedemnaście ", "osiemnaście ", "dziewiętnaście "]
setki = [ "", "sto ", "dwieście ", "trzysta ",
        "czterysta ", "pięćset ", "sześćset ",
        "siedemset ", "osiemset ", "dziewięćset " ]
rzedy = [["tysiąc ", "tysiące ", "tysięcy "],
         [ "milion ", "miliony ", "milionów "],
         ["miliard ", "miliardy ", "miliardów "]]

liczba =""
while(type(liczba) != int):
    try:
        liczba = int(input())
    except ValueError:
        print("Pisz bez liter i spacji.")




def ZamienNaSlowaRzedy(liczba):

    lista = []
    rzad = 0

    while (liczba > 0):
        jednosc = liczba % 10
        dziesiatka = liczba % 100
        setka = int((liczba % 1000) / 100)



        if(int((liczba % 1000)/10) == 0):
            #1 - tysiac
            if(jednosc == 1):
                lista.insert(0, rzedy[rzad][0])
            #2-4 tysiace
            elif(jednosc >= 2 and jednosc <= 4):
                lista.insert(0, rzedy[rzad][1])
            #5-9 tysiecy
            elif(liczba % 1000 != 0):
                lista.insert(0, rzedy[rzad][2])
            if(jednosc > 1):
                lista.insert(0,jednosci[jednosc])
        else:
            #10-19 nastki
            if(dziesiatka >= 10 and dziesiatka < 20):
                lista.insert(0,rzedy[rzad][2])
                lista.insert(0,nascie[dziesiatka % 10])
            else:
                #2-4 tysiace
                if(jednosc >= 2 and jednosc <= 4):
                    lista.insert(0,rzedy[rzad][1])
                #5-9 tysiecy
                elif(liczba % 1000 != 0):
                    lista.insert(0,rzedy[rzad][2])
                lista.insert(0,jednosci[jednosc])
                lista.insert(0,dziesiatki[int(dziesiatka / 10)])

            lista.insert(0,setki[setka])

        rzad+=1
        liczba = int(liczba / 1000)
        print(lista)

    return lista


def ZamienNaSlowa(liczba):

    lista = []
    jednosc = liczba % 10
    dziesiatka = liczba % 100
    setka = int((liczba % 1000) / 100)

    #11-19 nastki
    if (dziesiatka > 10 and dziesiatka < 20):
        lista.insert(0, nascie[jednosc])
    #20-99
    else:
        lista.insert(0, jednosci[jednosc])
        lista.insert(0, dziesiatki[int(dziesiatka / 10)])

    lista.insert(0, setki[setka])

    liczba = int(liczba / 1000)
    listaZRzedami = ZamienNaSlowaRzedy(liczba)
    listaZRzedami.extend(lista)

    wynik = ""
    for liczba in listaZRzedami:
        wynik += liczba


    print(wynik)






ZamienNaSlowa(liczba)





