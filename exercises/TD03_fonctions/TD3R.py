# temps[0] : (24) jours, temps[1]: (3600) heures, temps[2]: (60) minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return (temps[0]*24*3600+temps[1]*3600+temps[2]*60+temps[3])

temps = [3,23,1,34]
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours = seconde // (24*3600)
    reste = seconde % (24*3600)
    heures = reste // (3600)
    reste = reste % 3600
    minutes = reste // 60
    secondes = reste % 60
    return(jours,heures,minutes,secondes)
    
temps = secondeEnTemps(100000)
print(" ")
print("Seconde en temps :", temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

def plrs (temps, mot):
  if temps != 0:
    print(" ", temps, mot, end="")
  if temps > 1:
    print("s", end="")


def afficheTemps(temps):
    print(" ")
    plrs(temps[0], mot="jour")
    plrs(temps[1], mot="heure")
    plrs(temps[2], mot="minute")
    plrs(temps[3], mot="seconde")

afficheTemps(temps)

def demandeTemps():
    print(" ")
    Utps = [0,0,0,0]
    Utps[0] = int(input('Rentrez le nb de jour(s) : '))
    Utps[1] = int(input("Rentrez le nb d'heure(s) : "))
    Utps[2] = int(input("Rentrez le nb de minute(s) : "))
    Utps[3] = int(input("Rentrez le nb de seconde(s) : "))
    if Utps[1]>24 or Utps[2]>60 or Utps[3]>60:
      print("Une valeur rentrée n'est pas bonne")
    return (Utps[0], Utps[1], Utps[2], Utps[3])

afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
  return secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))

sommeTemps((2,3,4,25),(5,22,57,1))

def proportionTemps(temps,proportion):
  """Evalue une proportion d'un temps donné en reprenant les premières fonctions"""
  return (secondeEnTemps(int(tempsEnSeconde(temps)*proportion)))

afficheTemps(proportionTemps((2,0,36,0),0.2))

def proportionTemps(temps,proportion):
  """Evalue une proportion d'un temps donné en reprenant les premières fonctions"""
  return (secondeEnTemps(int(tempsEnSeconde(temps)*proportion)))

afficheTemps(proportionTemps(proportion = 0.2, temps=(2,0,36,0)))

def tempsEnDate(temps):
    jours, heures, minutes, secondes = temps
    annee = 1970+jours//365
    jours = jours%365
    return (annee, jours, heures, minutes, secondes)

temps = (370,23,1,34)
tempsEnDate(temps)

#import time
#def afficheDate(date = -1):
#  date=int(time.time(tempsEnSeconde))
#  print("Jour numéro", date[1], "de l'année", date[0], "à", str(date[2])+str(date[3])+":"+str(date[4]))  

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
#afficheDate(tempsEnDate(temps))
#afficheDate()
