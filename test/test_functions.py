from hypot.functions import addition, squared, sqroot, hypot

# test addition
def test_addition_int():
    assert addition(4,7) == 4


# test squared
def test_squared_odd():
    assert squared (-2) == 4


# test squared root
def test_squroot():
    assert sqroot(9) == 3


# test hypot
def test_hypot():
    assert hypot(3,4) == 5