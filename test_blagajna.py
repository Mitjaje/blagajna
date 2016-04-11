from blagajna import get_price

def testing_get_price():
    assert get_price("mleko") == 2.25 # zagotovi da bo to res
    assert get_price("kruh") == 1.68
    assert get_price("jajca") == 3.15
    assert get_price("sok") == 1.22
    assert get_price("salama") == 1.43
    assert get_price("jogurt") == 2.87
    return "testing_numbers_sum() passed successfully"

print testing_get_price()

