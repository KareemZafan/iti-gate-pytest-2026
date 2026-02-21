
## this is a test for calculator.py
import pytest
from src import calculator

myList =[(-1,1,0), (-100,90,-10),(-100,-90,-190),(-30,20,-10),(30,0,30)]

@pytest.mark.parametrize("a, b, expected",myList)
def test_add(a, b, expected):
  assert calculator.add(a,b) == expected



def test_subtract():
 assert calculator.subtract(-1, 1) == -2
 assert calculator.subtract(-100, 90) == -190
 assert calculator.subtract(-100, -90) == -10
 assert calculator.subtract(-30, 20) == -50
 assert calculator.subtract(30, 0) == 30

def test_multiply():
## arrange 
### act
## assert
 assert calculator.multiply(-1, 1) == -1
 assert calculator.multiply(-100, 90) == -9000
 assert calculator.multiply(-100, -90) == 9000
 assert calculator.multiply(-30, 20) == -600
 assert calculator.multiply(30, 0) == 0

@pytest.mark.RAMADN_RELEASE
def test_divide():
## arrange 
### act
## assert
 assert calculator.divide(-1, 1) == -1
 assert calculator.divide(-100, 90) == -1.1111111111111112
 assert calculator.divide(-100, -90) == 1.1111111111111112
 assert calculator.divide(-30, 20) == -1.5

 with pytest.raises(ZeroDivisionError):
     calculator.divide(6, 0)   

@pytest.mark.RAMADN_RELEASE
@pytest.mark.parametrize("input, output", [(100, 10), (625, 25), (0, 0), (-50, None), (-1, None)])
def test_square_root(input, output):
    assert calculator.get_square_root(input) == output

 

#  with pytest.raises(ValueError):
#      calculator.get_square_root(-50)   







