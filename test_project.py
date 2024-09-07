from project import AND, OR, NOT, NAND, NOR, XOR, XNOR

def main():
    test_AND()
    test_OR()
    test_NOT()
    test_NAND()
    test_NOR()
    test_XOR()
    test_XNOR()


def test_AND():
    assert AND(0, 0) == 0
    assert AND(0, 1) == 0
    assert AND(1, 0) == 0
    assert AND(1, 1) == 1

def test_OR():
    assert OR(0, 0) == 0
    assert OR(0, 1) == 1
    assert OR(1, 0) == 1
    assert OR(1, 1) == 1

def test_NOT():
    assert NOT(0) == 1
    assert NOT(1) == 0

def test_NAND():
    assert NAND(0, 0) == 1
    assert NAND(0, 1) == 1
    assert NAND(1, 0) == 1
    assert NAND(1, 1) == 0

def test_NOR():
    assert NOR(0, 0) == 1
    assert NOR(0, 1) == 0
    assert NOR(1, 0) == 0
    assert NOR(1, 1) == 0

def test_XOR():
    assert XOR(0, 0) == 0
    assert XOR(0, 1) == 1
    assert XOR(1, 0) == 1
    assert XOR(1, 1) == 0

def test_XNOR():
    assert XNOR(0, 0) == 1
    assert XNOR(0, 1) == 0
    assert XNOR(1, 0) == 0
    assert XNOR(1, 1) == 1

if __name__ == "__main__":

    main()
