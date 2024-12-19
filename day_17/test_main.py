from main import ChronoComputer
import pytest

@pytest.fixture
def computer():
    return ChronoComputer(0,0,0,[])

@pytest.mark.parametrize("i,result", [(0, 0), (1,1), (2,2), (3,3), (4,10),(5,20),(6,30)])
def test_combo(computer, i, result):
    computer.reg_a = 10
    computer.reg_b = 20
    computer.reg_c = 30
    assert computer.combo(i) == result
