import pytest

@pytest.fixture()
def before_after():
    print('\nBefore Test')
    yield None
    print('\nAfter Test')



def test_demo1():
    assert 1 == 1

def test_demo2(before_after):
    assert 2 == 3



# .\venv\Scripts\activate