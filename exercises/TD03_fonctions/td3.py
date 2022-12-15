def TpsSec(temps):
    return temps[0]*86400+temps[1]*3600+temps[2]*60+temps[3]

m_temps = [3, 23, 1, 34]

def SecTps (seconde: int) -> tuple:
    jours = seconde // 86400
    reste = seconde % 86400
    heures = reste // 3600
    reste = reste % 3600
    minutes = reste // 60
    reste = reste % 60
    return (jours, heures, minutes, reste)

temps = SecTps(100000)
print(m_temps[0],"jours", m_temps[1],"heures", m_temps[2], "minutes", m_temps[3], "secondes")

def plrs (mot: str, nombre: int) -> None:
    if nombre > 0:
        print("", nombre, mot, end="")
    if nombre > 1:
        print("s", end="")
    
def AffTps (m_temps):
    plrs(nombre = temps[0], mot = "Jour")
    plrs(nombre = temps[1], mot = "Heure")
    plrs(nombre = temps[2], mot = "Minute")
    plrs(nombre = temps[3], mot = "Seconde")

def demandeTps():
    jours = -1
    heures = -1
    minutes = -1
    secondes = -1
    while(jours<0):
        jours = int(input("Nbr de jours"))
    while(heures<0):
        heures = int(input("Nbr de heures"))
    while(minutes<0):
        minutes = int(input("Nbr de minutes"))
    while(secondes<0):
        secondes = int(input("Nbr de secondes"))

def sommeTps(temps1, temps2):
    return SecTps (TpsSec(temps1) + TpsSec(temps2))

AffTps(demandeTps((2, 3, 4, 25), (5, 22, 57, 1)))