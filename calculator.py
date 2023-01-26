kolvo = int(input("Колво число: "))
choslo = float(input("Введи число: "))
if kolvo < 2:
    print("Нужно больше 2")
i = 2
while i <= kolvo:
    vibor = input('Что делаем? ( + , - , * , /, ^): ')
    
    chislo2 = float(input("Введи число: "))
    if vibor == "+":
        choslo = choslo + chislo2
        print(f"Результат:  {choslo}")
    elif vibor == "-":
        choslo = choslo - chislo2
        print(f"Результат:  {choslo}")
    elif vibor == "*":
        choslo = choslo * chislo2
        print(f"Результат:  {choslo}")
    elif vibor == "/":
        if chislo2 == 0:
            print("Не нужно делить на ноль")
        else:
            choslo = choslo / chislo2
            print(f"Результат:  {choslo}")
    elif vibor == "^":
        choslo = choslo ** chislo2
        print(f"Результат:  {choslo}")
    i += 1

