def ist_sicher(bericht):
    zahlen = [int(ding) for ding in bericht.split()]
    
    def dampener(zahlen):
        n_anstieg = 0
        n_abfall = 0
        letzter_wert = zahlen[0]

        for i in range(1, len(zahlen)):
            aktueller_wert = zahlen[i]
            delta = abs(letzter_wert - aktueller_wert)

            if delta < 1 or delta > 3:
                return False  

            if letzter_wert > aktueller_wert:
                n_abfall += 1
            elif letzter_wert < aktueller_wert:
                n_anstieg += 1

            letzter_wert = aktueller_wert

 
        return not (n_anstieg > 0 and n_abfall > 0)

  
    if dampener(zahlen):
        return True

     
    for i in range(len(zahlen)):
       
        neue_zahlen = zahlen[:i] + zahlen[i+1:]
        if dampener(neue_zahlen):
            return True   

    return False

n_sicher = 0

with open("advent02.txt", "r") as file:
    for bericht in file:
        bericht = bericht.strip()   
        if ist_sicher(bericht):
            n_sicher += 1

print(n_sicher)
