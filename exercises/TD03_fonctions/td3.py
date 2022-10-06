#temps[0] : jours, temps[1]: heures, temps[2]: mintures, temps[3] : secondes
def TpsSec(temps):
    
    """Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    pass

temps=(3,23,1,34)
print(type(temps))
print(TpsSec(temps))

def SecTps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nbr de seconde passé en argument"""
    pass

temps = SecTps(100000)
print(temps[0], "jours", temps[1], "heures",temps[2], "minutes", temps[3], "secondes")