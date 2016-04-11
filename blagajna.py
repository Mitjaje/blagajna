items_prices = {
    "mleko": 2.25,
    "kruh": 1.68,
    "jajca": 3.15,
    "sok": 1.22,
    "salama": 1.43,
    "jogurt": 2.87
}

def get_price(item):
    if item in items_prices.keys():
        price = items_prices[item]
        return price
    else:
        return 0

if __name__ == "__main__":

    while True :
        item=raw_input("Izberi izdelek: ")
        price = get_price(item)
        if (price):
            print ("Cena izdelka je: %s" % price)
        else:
            print("Izdelka ni na zalogi.")