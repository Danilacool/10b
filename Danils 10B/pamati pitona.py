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


#-ievadi 3 vertibas (abc)
#noteikt vai var eksistēt trīstūris
a = int(input("ievadi malu a: "))
b = int(input("ievadi malu b: "))
c = int(input("ievadi malu c: "))

if a < b + c and b < a + c and c < a + b:
    print("eksistē")
else:
    print("neeksistē")












