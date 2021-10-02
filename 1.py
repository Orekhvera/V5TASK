number = input('Введите число: ') 
try:
    int(number)
    k = 1
    for letter in number: 
        if int(letter) % 2 == 0:
            k *= int(letter)
    print("Произведение четных цифр чила: ", k)
except:
    print ("Ошибка!!!")

