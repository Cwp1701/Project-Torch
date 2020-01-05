from Character import Chr

try:
    Chr1 = Chr(100, 30, True)
    Chr2 = Chr(100, 30, True)
    Chr3 = Chr(100, 30, True)
except SyntaxError as err:
    print(err)
except TypeError as err:
    print(err)
except OverflowError as err:
    print(err)
except:
    print("Unkown error")

ChrSelect = input("Chose Character")

def losehealth():
    print("")

















