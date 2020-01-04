from Character import character

Characters = [

    character(100, 30, True)

]

try:

    print(Characters[0])

except SyntaxError as err:
    print(err)


