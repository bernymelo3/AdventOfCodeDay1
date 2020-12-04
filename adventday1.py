def parte1(numeros, set_numeros):
    for numero in numeros:
        if 2020 - numero in set_numeros:
            return numero * (2020 - numero)


def parte2(numeros, set_numeros):
    for numero in numeros:
        for num2 in numeros:
            if (2020 - numero - num2) in set_numeros:
                return numero * (2020 - numero - num2) * num2


with open("input.txt") as _file:
    numeros = [int(line) for line in _file]
    set_numeros = set(numeros)

    print("Part 1", parte1(numeros, set_numeros))
    print("Part 2", parte2(numeros, set_numeros))

