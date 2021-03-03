units = {
        0:"",
        1:"one ",
        2:"two ",
        3:"three ",
        4:"four ",
        5:"five ",
        6:"six ",
        7:"seven ",
        8:"eight ",
        9:"nine ",
        10:"ten ",
        11:"eleven ",
        12:"twelve ",
        13:"thirteen ",
        14:"fourteen ",
        15:"fifteen ",
        16:"sixteen ",
        17:"seventeen ",
        18:"eighteen ",
        19:"nineteen ",
}

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
scales = ["thousand ", "million ", "billion ", "trillion "]


number =""
while(type(number) != int):
    try:
        number = int(input())
    except ValueError:
        print("Write without letters and spaces.")



def ConvertNumbersToWordsScales(number):
    list = []
    scale = 0

    while (number > 0):
        unit = number % 10
        ten = number % 100
        hundreds = int((number % 1000) / 100)

        if (ten >= 9 and ten < 20):
                list.insert(0, scales[scale])
                list.insert(0, units[ten])
        elif (number % 1000 != 0):
                    list.insert(0, scales[scale])
        list.insert(0, units[unit])
        list.insert(0, tens[int(ten / 10)])
        if(tens[int(ten / 10)] != ''):
            list.insert(1,'-')

        list.insert(0, units[hundreds])
        if (units[hundreds] != ''):
                list.insert(1, "hundred ")

        scale += 1
        number = int(number / 1000)

    return list



def ConvertNumbersToWords(number):
    lista = []
    unit = number % 10
    ten = number % 100
    hundreds = int((number % 1000) / 100)


    if (ten > 9 and ten < 20):
        lista.insert(0, units[ten])

    else:
        lista.insert(0, "-" + units[unit])
        lista.insert(0, tens[int(ten / 10)])
    lista.insert(0, units[hundreds])
    if(units[hundreds] != ''):
        lista.insert(1,"hundred ")

    number = int(number / 1000)
    listWithScales = ConvertNumbersToWordsScales(number)
    listWithScales.extend(lista)

    result = ""
    for word in listWithScales:
        result += word
    print(result)

ConvertNumbersToWords(number)


