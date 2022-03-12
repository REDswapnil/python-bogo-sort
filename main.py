from random import shuffle


def bogo_sort(num_list: list) -> list:
    print(f'Sorting list :: {num_list}')
    counter: int = 0
    while not check_sorted(num_list):
        shuffle(num_list)
        counter = counter + 1
    print(f'List sorted after mere {counter} iterations !!')
    return num_list


def check_sorted(num_list: list) -> bool:
    return all(a <= b for a, b in zip(num_list, num_list[1:]))


if __name__ == '__main__':
    test_list: list = [2, 4, 7, 1, 3, 9, 6, 8]
    with open('banner.txt', 'r') as banner:
        print(''.join([line for line in banner]))

    print('Running the prodigy of sorting algorithms :: BOGO-SORT')
    print(f'Sorted List :: {bogo_sort(test_list)}')
