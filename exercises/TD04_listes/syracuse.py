carre_mag = [[4, 14, 15, 1]]
carre_pas_mag = []
for num_ligne in range(len(carre_mag)):
    carre_pas_mag.append([])
    for num_colonne in range(len(carre_mag[num_ligne])):
        carre_pas_mag[num_ligne].append(carre_mag[num_ligne][num_colonne])

carre_pas_mag[3][2] = 7

def affcarre(carre):
    for ligne in carre:
        print(ligne)
    print()
affcarre(carre_mag)
affcarre(carre_pas_mag)