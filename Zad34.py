def pretraga(games, developer, rating):
    
    for game in games:
        name, dev, release_date, game_rating = game
        if dev == developer and game_rating > rating:
            print(game)

lista = [("Gta", "R", 2013, 9), ("GT7", "S", 2021,8)]
pretraga(lista, "R", 7)
        