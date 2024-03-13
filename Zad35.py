zahtjev = "GOOG 300 542.0 B, ABC 100 400.3 S"
def broker(zahtjevi):
    kupljeni = 0
    prodati = 0
    zahtjev = zahtjevi.split(",")
    print(zahtjev)
    for format in zahtjev:
        format.strip()
        format = format.split(" ")
        if format[-1] == "B":
            kupljeni = int(format[1]) * float(format[2])
        else:
            prodati = int(format[1]) * float(format[2])
    print(f"Buy: {kupljeni} Sell: {prodati}")
broker(zahtjev)