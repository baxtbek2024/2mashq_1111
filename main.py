
#1-misol
satrlar = ["salom", "python", "kitob"]
uzunliklar = list(map(lambda s: len(s), satrlar))
print(uzunliklar)

#2-misol
sonlar = [1, 2, 3, 4, 5, 6, 7]
toq_kvadrat = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, sonlar)))
print(toq_kvadrat)

#3-misol
royxat = [2, 4, 6, 8]
natija = list(map(lambda x: x[0]*x[1], enumerate(royxat)))
print(natija)

#4-misol
palindrom = lambda s: s == s[::-1]
satrlar = ["level", "python", "madam", "hello"]
natija = list(map(palindrom, satrlar))
print(natija)

#5-misol
sonlar = [2, 5, 6, 7, 10, 12]
natija = list(map(lambda x: x*3, filter(lambda x: 5 <= x < 10, sonlar)))
print(natija)

