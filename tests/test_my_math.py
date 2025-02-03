import pytest

from src.my_math import sum, multiply, difference, absolute_sum, calculate_birth_year

def test_sum():
    res = sum(1,1)
    assert res == 2

# Work together
## Test multiply

def test_multipy():
    res = multiply(2, 2)
    assert res == 4

# Check for understanding
## Test difference

def test_difference():
    res = difference(2, 1)
    assert res == 1

# Work together
## Test absolute sum

def test_absolute_sum():
    res = absolute_sum(-2, 4)
    assert res == 6 
def test_itshoudlreturnpositivenumber():
    rest = absolute_sum(1, 2)
    assert rest == 3
def test_botharenegativenumbers():
    res = absolute_sum(-1, -2)
    assert res == 3
def test_whateveritisnow():
    res = absolute_sum(1, -5)
    assert res == 6
# Check for understanding
## Test calculate age

def test_calculate_birth_year():
    res = calculate_birth_year(2040, 98, 'no')
    assert res == 1942
def test_calculate_birth_year_2():
    res = calculate_birth_year(2025, 25, 'yes')
    assert res == 2000