filmovi = ({"film":"Godfather", "br_pozitivni": 1000, "br_negativni": 500},{"film":"Shrek", "br_pozitivni": 1500, "br_negativni": 500})
def najbolji_odnos(filmovi):
    najrev = 0 #Cuva najbolji odnos pozivnih i negativnih komentara
    najrevfilm = None
    for film in filmovi:
        odnos = film["br_pozitivni"] / film["br_negativni"]
        if odnos > najrev:
            najrevfilm = film
    print(f"Film sa najboljim odnosom pozitivnih i negativnih kometara je {najrevfilm['film']}")
    
najbolji_odnos(filmovi)


def ime_sa_pocetkom(filmovi, search_term):
    for film in filmovi:
        if film['film'].startswith(search_term):
            print(film)

ime_sa_pocetkom(filmovi, 'Sh')