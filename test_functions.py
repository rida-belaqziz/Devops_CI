#Belaqziz Rida
from unittest import result
from main import count_char, check_if_maj, check_if_special, check_if_valid_password


#TEST UNITAIRE

def test_count_char():
    input = "Bonjour"
    expected = 7
    result = count_char(input)
    assert expected == result

def test_check_if_maj():
    input1 = "BonJouR"
    input2 = "bonjour"

    expected1 = True
    expected2 = False

    result1 = check_if_maj(input1)
    result2 = check_if_maj(input2)

    assert expected1 == result1
    assert expected2 == result2


def test_if_special():
    input1 = "Bon@ou!"
    input2 = "bonjour"

    expected1 = True
    expected2 = False

    result1 = check_if_special(input1)
    result2 = check_if_special(input2)

    assert expected1 == result1
    assert expected2 == result2

#TEST CI    

def test_check_if_valid_password():
    input1 = "Bon@ou!"
    input2 = "bonjour_S@Lut!"
    input3 = "bonjour"

    expected1 = False
    expected2 = True
    expected3 = False

    result1 = check_if_valid_password(input1)
    result2 = check_if_valid_password(input2)
    result3 = check_if_valid_password(input3)


    assert expected1 == result1
    assert expected2 == result2
    assert expected3 == result3