#
# failas = open('./file.txt')
# nuskaitytas_tekstas = failas.read()
# print(nuskaitytas_tekstas)
# failas.close()
#
#
# failas = open('./file.txt')
# nuskaitytas_tekstas = failas.read()
# print("Nuskaitytas:\n",nuskaitytas_tekstas)
# print()
#
# kitas_tekstas = failas.read()
# print("kitas:", kitas_tekstas)
#
# failas.close()

# failas = open('./file.txt')
# nuskaitytas_tekstas = failas.read()
# print("Nuskaitytas:",nuskaitytas_tekstas)
# print()
#
# failas.seek(0)
# per_nauja = failas.read()
# print("Naujas:", per_nauja)
# failas.close()

# failas = open('./file.txt')
# print("Nuskaitytas tekstas", failas.read())
# failas.close()

# with open('./file.txt') as failas:
#     tekstas = failas.read()
#     print(tekstas)
#     print()
#     failas.seek(10)
#     atnaujinimas = failas.read()
#     print("Naujas: ", atnaujinimas)


# with open('./file.txt') as failas:
#     eilute = failas.readline()
#     print(eilute)
#     eilute = failas.readline()
#     print(eilute)
#     eilute = failas.readline()
#     print(eilute)

# with open('./file.txt') as failas:
#     visas = failas.readlines()
#     print(visas)

# with open('./file.txt') as failas:
#     visas = failas.readlines()
#     print("Visas tekstas:",visas)
#     pertvarka = [eilute [:-1] for eilute in visas]
#     print("Sutvarkytas tekstas:", pertvarka)

# with open('./file.txt') as failas:
#     visas = failas.read().splitlines()
#     print(visas)

# with open('./file.txt') as failas:
#     txt = failas.read()
#     txt1 = failas.readline()
#     txt2 = failas.readlines()
#     print(type (txt))
#     failas.seek(0)
#     print(type(txt1))
#     failas.seek(0)
#     print(type(txt2))

# eilutes = []
#
# with open('./file.txt') as failas:
#     while True:
#         eilute = failas.readline().rstrip('\n')
#         if not eilute:
#             break
#         print("Nuskaityta eilute:", eilute)
#         eilutes.append(eilute)
#
# print(eilutes)

# with open('./file.txt', 'w') as failas:


# studentai = []
#
# with open('./students.txt', encoding="utf8") as failas:
#     for eilute in failas:
#         if not eilute:
#             continue
#         eilute = eilute.rstrip('\n')
#         isskaidyta = eilute.split(';')
#         studentas = dict(
#             vardas = isskaidyta[0],
#             pavarde = isskaidyta[1],
#             amzius = isskaidyta[2],
#             mokykla = isskaidyta[3],
#             vidurkis = isskaidyta[4]
# )
# studentai.append(studentas)
# print(studentai)

# with open('./file.txt', 'w') as file:
#     file.write('I WAS HERE FIRST')
#
# with open('./file.txt', 'r+') as file:
#     file.write(':)')
#     file.seek(10)
#     file.write(':(')