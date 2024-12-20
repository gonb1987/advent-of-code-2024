from main import ChronoComputer
import pytest


@pytest.fixture
def computer():
    return ChronoComputer(0, 0, 0, [])


@pytest.mark.parametrize("i,result", [(0, 0), (1, 1), (2, 2), (3, 3), (4, 10), (5, 20), (6, 30)])
def test_combo(computer, i, result):
    computer.reg_a = 10
    computer.reg_b = 20
    computer.reg_c = 30
    assert computer.combo(i) == result

adv_program = [
    (20, [0,2], 5),
    (35, [0,4], 0),
    (58, [0,3], 7),
    (26, [0,5], 26)
]

@pytest.mark.parametrize('reg_a,program,result', adv_program)
def test_adv(computer, reg_a, program, result):
    computer.program = program
    computer.reg_a = reg_a
    computer.execute()
    assert computer.reg_a == result

bxl_program = [
    (11, [1,2], 9),
    (35, [1,4], 39),
    (58, [1,3], 57),
    (26, [1,5], 31)
]

@pytest.mark.parametrize('reg_b,program,result', bxl_program)
def test_bxl(computer, reg_b, program, result):
    computer.reg_b = reg_b
    computer.program = program
    computer.execute()
    assert computer.reg_b == result


bst_program = [
    ([2,2], 2),
    ([2,4], 4),
    ([2,3], 3),
    ([2,6], 1)
]
@pytest.mark.parametrize('program,result', bst_program)
def test_bst(computer, program, result):
    computer.reg_a = 100
    computer.reg_b = 202
    computer.reg_c = 305
    computer.program = program
    computer.execute()
    assert computer.reg_b == result

jnz_program = [
    (0, 5, 2),
    (1, 7, 7)
]
@pytest.mark.parametrize('reg_a,operand,result', jnz_program)
def test_jnz(computer, reg_a, operand, result):
    computer.reg_a = reg_a
    computer.jnz(operand)
    assert computer.pointer == result


def test_bxc():
    assert False


def test_out():
    assert False


def test_bdv():
    assert False


def test_cdv():
    assert False


def test_choose_func():
    assert False
