import pprint

from operator import pow


def pow_list(*args, power=2) -> list:
    """Return list of powered numbers
    :param power: power value (int)
    """
    arr = []
    power_list = []
    for i in args:
        try:
            arr.append(int(i))
        except ValueError:
            print(i, ' is not an integer, missed')
    for _ in range(len(arr)):
        power_list.append(power)
    result_list = list(map(pow, power_list, arr))
    pprint.pprint(result_list)
    return result_list


if __name__ == '__main__':
    pow_list(1, 'kl', 3, power=8)
