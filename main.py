#1
juft = [1, 2, 3, 4, 5, 6, 7, 8]
print(juft)

juft2 = list(filter(lambda el: el % 2 == 0, juft))
print(juft2)


#2
toq = [10, 15, 20, 25, 30]
print(toq)

toq2 = list(filter(lambda el: el % 2 != 0, toq))
print(toq2)


#3
musbat = [-5, 3, -2, 7, -1, 0, 9]
print(musbat)

musbat2 = list(filter(lambda el: el > 0, musbat))
print(musbat2)


#4
manfiy = [4, -3, 0, -7, 8, -1]
print(manfiy)

manfiy2 = list(filter(lambda el: el < 0, manfiy))
print(manfiy2)


#5
katta = [-2, 0, 5, 8, -1]
print(katta)

katta2 = list(filter(lambda  el: el > 0, katta))
print(katta2)


#6
son = [1, 6, 3, 8, 2, 10]
print(son)

son2 = list(filter(lambda el: el > 5, son))
print(son2)


#7
kichik = [12, 5, 7, 20, 3, 15]
print(kichik)

kichik2 = list(filter(lambda el: el < 10, kichik))
print(kichik2)


#8
faqat = [3, 5, 9, 10, 12, 14]
print(bolish)

bolish2 = list(filter(lambda el: el % 3 == 0, bolish))
print(bolish2)


#9
bolish = [6, 8, 12, 15, 18, 20]
print(bolish)

bolish2 = list(filter(lambda el: el % 2 == 0 and el % 3 == 0, bolish))
print(bolish2)


#10
teng = [0, 1, 2, 0, 3, 0, 4]
print(teng)

teng2 = list(filter(lambda el: el != 0, teng))
print(teng2)
