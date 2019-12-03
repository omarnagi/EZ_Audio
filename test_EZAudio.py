def mult(a,b):
    c=a*b
    return c

def add(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def div(a,b):
    c=a/b
    return c

def isEven(a):
    if (a%2)==0:
        return 1
    else:
        return 0

def isOdd(a):
    if (a%2)==0:
        return 0
    else:
        return 1


def test_mult():
    case=mult(4,2)
    assert case==8
def test_add():
    case=add(4,2)
    assert case==6
def test_sub():
    case=sub(4,2)
    assert case==2
def test_div():
    case=div(4,2)
    assert case==2
def test_isEven():
    case=isEven(4)
    assert case==1
def test_isOdd():
    case=isOdd(4)
    assert case==0