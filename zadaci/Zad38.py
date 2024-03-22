filmovi = ({"naziv":"Godfather", "br_pozitivni": 2500, "br_negativni": 500},{"naziv":"Shrek", "br_pozitivni": 1500, "br_negativni": 500})
def najbolji_odnos(filmovi):
    najrevfilm = None
    najodnos = 0
    for film in filmovi:
        odnos = film["br_pozitivni"] / film["br_negativni"]
        if odnos > najodnos:
            najodnos = odnos
            najrevfilm = film
    print(f"Film sa najboljim odnosom pozitivnih i negativnih kometara je {najrevfilm['naziv']}")
    
najbolji_odnos(filmovi)


def ime_sa_pocetkom(filmovi, search_term):
    for film in filmovi:
        if film['naziv'].startswith(search_term):
            print(film)

ime_sa_pocetkom(filmovi, 'Sh')