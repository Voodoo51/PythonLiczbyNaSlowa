import PL
import EN

whichLanguage = ""
while(type(whichLanguage) != int):
    try:
        print("Zamiana liczb na slowa:")
        print("1 - po polsku,")
        print("2 - po angielsku")

        whichLanguage = int(input())

        if(whichLanguage > 2 or whichLanguage < 0):
            print("Nie ma takiej opcji.")

    except ValueError:
        print("Nieodpowniedni znak.")


number = ""

if(whichLanguage == 1):
            text = PL.text
            wrongText = PL.wrongText
            Converter = PL.ZamienNaSlowa
elif(whichLanguage == 2):
            text = EN.text
            wrongText = EN.wrongText
            Converter = EN.ConvertNumbersToWords

while (type(number) != int):
    try:
        number = int(input(text))
    except ValueError:
        print(wrongText)


print(Converter(number))