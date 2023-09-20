def routes_index(aa):
    if aa == "AUAU":
        return "/ausbildung"
    elif aa == "EQ":
        return "/ausbildung"
    elif aa == "UM":
        return "/umschueler"
    elif aa == "BGJH":
        return "/holztechnik"
    elif aa == "BGJZ":
        return "/holztechnik"
    elif aa == "BIK":
        return "/Berufsintegrationsklasse"
    else:
        return "/404"
