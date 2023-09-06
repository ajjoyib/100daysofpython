def average_calculator(royxat):
    yigindi = 0
    for element in royxat:
        yigindi += element
    average = yigindi / len(royxat)
    return average


def ctof(ctemp):
    ftemp = (ctemp * 9 / 5) + 32
    return ftemp
