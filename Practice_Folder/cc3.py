
def power(i: int) -> int:
    return i**2


def power_of_set_range(mini: int, maxi: int) -> None:
    for i in range(mini, maxi+1):
        print(i, i**2, sep=' -> ')


for i in range(300):
    print(i, power(i), sep=' -> ')

print(power_of_set_range(4, 400))

