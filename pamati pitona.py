# print("čau pasaule") #izvade ir PRINT/ Viss kas ir ķepiņās ir teksts

# vards="Danila" # zilais ir mainīgais ar to var kk veikt
# print(vards) # izvadot mainīgo rādīs to kas ir mainīgajā

# print(f"Mani sauc {vards}")

# skaits=6
# print(skaits)
# print(skaits+3)
# print(skaits/3)
# print(skaits%3)
# print(skaits//3)
# print(skaits*3)
# print(skaits**3)

# rezult = skaits**3
# print(rezult)

# nosaukums = input("ievadi  nosaukumu")# input ir tas kur kk var uzrakstīt
# print(f"tu ievadiji {nosaukums}")


# skaitlis = int(input("ievadi: "))#int jeb integer - vesels skaitlis/ input kur es pats varēšu kk ievadīt
# print(f"pieskaitot 5 sanāk {skaitlis + 5}")#f ir darbība, jeb tas kas ir pierakstīts mainīgajā

# if skaitlis > 5:#if ir sazarojums
#     print(f"{skaitlis}sk lielāks par 5")
# elif skaitlis == 5:#elif ir papildus nosacijums
#     print(f"{skaitlis}sk vienāds ar 5")
# else:# else ir pretēlā gadījumā no if
#    print(f"{skaitlis} mazāks par 5")

# #1. Tiek ievadīts skaitlis. Programa nosaka, vai tas ir lielāks par 0, mazāks vai vienāds.

# x = int(input("ievadi skaitli: "))

# if x > 0:
#     print(f"{x} sk lielāks par 0") #f ir ievade
# elif x == 0:
#     print(f"{x} sk vienāds ar 0")
# else:
#     print(f"{x} mazāks par 0")


# y = int(input("ievadi skaitli no 1-7: "))

# if y > 5:
#     print(f"{y} BRĪVDIENAAA!!!") #f ir ievade
# else:
#     print(f"{y} Darba diena :(")

# if y == 1:
#     print("pirmdiena")
# elif x == 2:
#     print("otrdiena")
# elif x == 3:
#     print("trešdiena")
# elif x == 4:
#     print("ceturtdiena")
# elif x == 5:
#     print("piekdiena")
# elif x == 6:
#     print("sestdiena")
# elif x == 7:
#     print("svētdiena")


# #-ievadi 3 vertibas (abc)
# #noteikt vai var eksistēt trīstūris
# a = int(input("ievadi malu a: "))
# b = int(input("ievadi malu b: "))
# c = int(input("ievadi malu c: "))

# if a < b + c and b < a + c and c < a + b:
#     print("eksistē")
# else:
#     print("neeksistē")

# # 3 ievadi trīs skaitļus





# 1. Tiek ievadīts skaitlis. Programma nosaka, vai tas ir lielāks par nulli, mazāks vai vienāds.

# x = int(input("Skaitlis: "))

# if x == 0:
#    print("vienāds ar 0")
# elif x > 0:
#    print("pozitīvs")
#    if x == 3:
#       print("x ir 3")
# else:
#    print("negatīvs")




# 2. Ievadīts dienas numurs (1-7). Programma nosaka
#    1) vai tā ir darba diena vai brīvdiena
#    2) dienas nosaukumu

# d = int(input("dienas numurs: "))

# if d == 1:
#    print("pirmdiena")
# elif d == 2:
#    print("otrdiena")
# elif d == 3:
#    print("trešdiena")
# elif d == 4:
#    print("ceturtdiena")
# elif d == 5:
#    print("piektdiena")
# elif d == 6:
#    print("sestdiena")
# else:
#    print("svētdiena")


# if d > 5:
#    print("brīvdiena!")
# else: 
#    print("darba diena")






# 3. Ievadītas 3 vērtības (a, b, c). 
#    Noteikt, vai ar šādiem malu garumiem var eksistēt trijstūris.

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if a + b > c:
#    if b + c > a:
#       if c + a > b:
#          print("Eksistē")
#       else: 
#          print("Neeksistē") 
#    else: 
#       print("Neeksistē")
# else: 
#    print("Neeksistē")

# if a + b > c and b + c > a and c + a > b:
#    print("Eksistē")
# else: 
#    print("Neeksistē")





# 4. Noteikt, vai ievadītais skaitlis ir pāra vai nepāra.

# skaitlis = int(input("skaitlis: "))

# if skaitlis % 2 != 0:
#    print("nepāra")
# else:
#    print("pāra")







# 5. Ievadīti trīs skaitļi. No tiem izvadīt lielāko.

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if a >= b and a >= c:
#    print("a ir lielākais")
# elif b >= a and b >= c:
#    print("b ir lielākais")
# else:
#    print("c ir lielākais")






# 6. Trīs skaitļi. Aprēķināt kvadrātvienādojuma saknes, 
#    ja šie skaitļi ir koeficienti a, b, c.

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# d = b ** 2 - 4 * a * c

# if d < 0:
#     print("sakņu nav!")
# elif d == 0:
#     print(f"x = {-b/(2*a)}")
# else:
#     print(f"x1 = {(-b+d**0.5)/(2*a)}")
#     print(f"x2 = {(-b-d**0.5)/(2*a)}")







# 7. Ievada skaitli. Noteikt mazāko iespējamo nominālu 
#    vērtību un skaitu, lai iegūtu ievadīto skaitli.
#    97 -> 4 1 1 1 0

# sk = int(input("skaitlis: "))

# # cik reizes skaitlī ieiet 20
# divdesmitniekuSkaits = sk // 20 
# # cik paliek pāri, kad 20nieka banknotes noņem
# sk = sk - divdesmitniekuSkaits * 20 

# desmitniekuSkaits = sk // 10
# sk = sk - desmitniekuSkaits * 10

# piecukuSkaits = sk // 5
# sk = sk - piecukuSkaits * 5

# divSkaits = sk // 2
# sk = sk - divSkaits * 2

# print(divdesmitniekuSkaits, desmitniekuSkaits, piecukuSkaits, divSkaits, sk)









# 8. Ievadīts trīsciparu skaitlis. Iegūt ciparu summu. 463 -> 13

# sk = int(input("trisciparu skaitlis: ")) # 463

# pedejais = sk % 10 # 3
# sk = (sk - pedejais) // 10 # 46

# videjais = sk % 10 # 6
# sk = (sk - videjais) // 10 # 4

# print(sk, videjais, pedejais) # 4 6 3
# print(sk + videjais + pedejais) # 13








# 9. Trīscipara skaitlim noteikt lielāko ciparu (#5; #8)

# sk = int(input("trisciparu skaitlis: ")) # 463

# pedejais = sk % 10 # 3
# sk = (sk - pedejais) // 10 # 46

# videjais = sk % 10 # 6
# pirmais = (sk - videjais) // 10 # 4

# print(pirmais, videjais, pedejais) # 4 6 3

# if pedejais >= videjais and pedejais >= pirmais:
#    print("pēdējais ir lielākais")
# elif videjais >= pirmais and videjais >= pedejais:
#    print("vidējais ir lielākais")
# else:
#    print("pirmais ir lielākais")






# 10. Dots datums un mēnesis. Noteikt, vai tāds eksistē. 
#     4, 5 -> eksistē
#     30, 2 -> neeksistē
#     31, 5 -> eksistē
#     31, 9 -> neeksistē

# diena = int(input("ievadi dienu: "))
# menesis = int(input("ievadi mēnesi: "))

# 2 -> 29
# 4, 6, 9, 11 -> 30
# visi pārējie -> 31

# if menesis == 2:
#     if diena < 30:
#         print("eksistē")
#     else:
#         print("neeksistē")
# elif menesis == 4 or menesis == 6 or menesis == 9 or menesis == 11:
#     if diena < 31:
#         print("eksistē")
#     else:
#         print("neeksistē")
# elif diena < 32:
#     print("eksistē")
# else:
#     print("neeksistē")






# 11. Ievada maksimālo punktu skaitu un iegūto punktu skaitu. Programma nosaka atzīmi.

# 40/100 -> 4

# iegutie_punkti = int(input("cik punkti tika ieguti: "))
# max_punkti = int(input("cik punktus varēja iegūt: "))

# print(f"atzīme: {iegutie_punkti * 10 // max_punkti}")

# <FV>







# 12. Ievadīti trīs skaitļi. Noteikt amplitūdu.
#     https://ej.uz/2u3b

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if a >= b and a >= c:
#     if b >= c:
#       print(a - c)
#     else:
#        print(a - b)
# elif b >= a and b >= c:
#     if a >= c:
#        print(b - c)
#     else:
#        print(b - a)
# else:
#     if a >= b:
#        print(c - a)
#     else:
#        print(c - b)

# print(max(a, b, c) - min(a, b, c))







# 13. Noteikt, vai ievadītais skaitlis dalās ar 3, ar 5 vai ar abiem.
#     https://ej.uz/1f9t

# skaitlis = int(input("skaitlis: "))

# if skaitlis % 15 == 0:
#     print("dalās ar abiem")
# elif skaitlis % 5 == 0:
#     print("dalās ar 5")
# elif skaitlis % 3 == 0:
#     print("dalās ar 3")
# else:
#     print("nedalās ne ar 5, ne 3")

# </FV>







# 14. Ievadīts trīsciparu skaitlis. 
#     Noteikt skaitļa ciparu summas vid. aritm.
#     597 -> 7

# sk = int(input("trisciparu skaitlis: ")) # 463

# vieni = sk % 10 # 3
# sk = (sk - vieni) // 10 # 46

# desmiti = sk % 10 # 6
# simti = (sk - desmiti) // 10 # 4

# print((simti + desmiti + vieni) / 3) # (4 + 6 + 3) / 3









# 15. Dots dienas numurs gadā. 
#     Noteikt, vai tā ir pāra vai nepāra nedēļa.
#     Pieņemt, ka pirmā diena ir pirmdiena.
#     5 -> nepāra
#     40 -> nepāra

# dienas_nr = int(input("ievadi dienas numuru: "))
# nedelas_pagajusas = dienas_nr // 7

# if dienas_nr % 7 > 0:
#     nedelas_pagajusas += 1

# if nedelas_pagajusas % 2 == 0:
#     print("pāra nedēļa")
# else:
#     print("nepāra nedēļa")








# 16. Ievadīti divi cipari. 
#     Izvilkt kvadrātsakni no skaitļa,
#     kas satur šos divus ciparus.
#     4 un 9 -> 7

# cipars1 = int(input("ievadi pirmo ciparu: "))
# cipars2 = int(input("ievadi otro ciparu: "))

# skaitlis = cipars1 * 10 + cipars2

# print(skaitlis ** 0.5)















# 17. Ievadīti divi cipari. Izveidot no tiem pāra skaitli, 
#     ja tas ir iespējams. Ja nav, tad izveidojam pāra
#     skaitli, saskaitot ciparus.
#     4, 5 -> 54
#     2, 0 -> 20 vai 2
#     7, 5 -> 12

# cipars1 = int(input("ievadi pirmo ciparu: "))
# cipars2 = int(input("ievadi otro ciparu: "))

# if cipars1 % 2 == 0:
#     print(cipars2 * 10 + cipars1)

# elif cipars2 % 2 == 0:
#     print(cipars1 * 10 + cipars2)

# else:
#     print(cipars1 + cipars2)






