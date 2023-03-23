summ = 0
summ1 = 0
summ2 = 0
summ3 = 0
summ4 = 0
summ5 = 0
summ6 = 0
summ7 = 0
summ8 = 0
summ9 = 0
summ10 = 0
summ11 = 0
summ12 = 0

for i in range(1, 13): 
    if i == 1 :
        summ1 = sum(map(int, str(12345678910111213141516171819202122232425262728293031)))
        print('Январь: ', summ1)
    if i == 2:
        summ2 = sum(map(int, str(1234567891011121314151617181920212223242526272829)))
        print('Февраль: ', summ2)
    if i == 3:
        summ3 = sum(map(int, str(12345678910111213141516171819202122232425262728293031)))
        print('Март: ', summ3)
    if i == 4:
        summ4 = sum(map(int, str(123456789101112131415161718192021222324252627282930)))
        print('Апрель: ', summ4)
    if i == 5:
        summ5 = sum(map(int, str(12345678910111213141516171819202122232425262728293031)))
        print('Май: ', summ5)
    if i == 6:
        summ6 = sum(map(int, str(123456789101112131415161718192021222324252627282930)))
        print('Июнь: ', summ6)
    if i == 7:
        summ7 = sum(map(int, str(12345678910111213141516171819202122232425262728293031)))
        print('Июль: ', summ7)
    if i == 8:
        summ8 = sum(map(int, str(12345678910111213141516171819202122232425262728293031)))
        print('Август: ', summ8)
    if i == 9:
        summ9 = sum(map(int, str(123456789101112131415161718192021222324252627282930)))
        print('Сентябрь: ', summ9)
    if i == 10:
        summ10 = sum(map(int, str(12345678910111213141516171819202122232425262728293031)))
        print('Октябрь: ', summ10)
    if i == 11:
        summ11 = sum(map(int, str(123456789101112131415161718192021222324252627282930)))
        print('Ноябрь: ', summ11)
    if i == 12:
        summ12 = sum(map(int, str(12345678910111213141516171819202122232425262728293031)))
        print('Декабрь: ', summ12)

    i += 1

summ = summ1 + summ2 + summ3 + summ4 + summ5 + summ6 + summ7 + summ8 + summ9 + summ10 + summ11 + summ12
print(summ)