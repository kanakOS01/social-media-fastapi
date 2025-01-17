from app.calculations import add

def test_add():
    sum = add(1, 3)
    assert sum == 4