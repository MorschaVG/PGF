def formatteer_namen (namen):
    """Neemt een lijst namen en zorgt dat deze met hoofdletter beginnen én gescheiden worden door komma's, behalve 
    de laatste waarde, die wordt gescheiden door het woord 'en'"""
    namen = [naam.capitalize() for naam in namen]

    if not namen:
        return ""
    elif len(namen) == 1:
        return namen[0]
    elif len(namen) == 2:
        return f"{namen[0]} en {namen[1]}"
    else:
        return f"{', '.join(namen[:-1])} en {namen[-1]}"

namenlijst = ["Morscha", "Merel", "Franco", "Juanita"]
result = formatteer_namen(namenlijst)
print(result)


