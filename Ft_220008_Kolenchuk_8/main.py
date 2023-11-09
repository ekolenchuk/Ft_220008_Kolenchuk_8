import number_name


def partition(nums, low, high, indexes):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]
        indexes[i], indexes[j] = indexes[j], indexes[i]


def quick_sort(nums, indexes):
    def _quick_sort(items, low, high, indexes):
        if low < high:
            split_index = partition(items, low, high, indexes)
            _quick_sort(items, low, split_index, indexes)
            _quick_sort(items, split_index + 1, high, indexes)

    _quick_sort(nums, 0, len(nums) - 1, indexes)


def fill_list_indexes(count):
    res = []
    for i in range(count):
        res.append(count + 1)
    return res


def fill_lists(input_str):
    f = 0
    for element in input_str:
        if element == '-':
            f += 1
            continue
        if f == 0:
            continue
        if f == 1:
            list_of_km.append(int(element))
            continue
        if f == 2:
            list_of_rub.append(int(element))
            continue


def queue_taxi(indexes_of_km, indexes_of_rub):
    count = len(indexes_of_rub)
    result_indexes = []
    for i in range(count):
        for index in indexes_of_km:
            if index == i + 1:
                result_indexes.append(indexes_of_rub[indexes_of_km.index(index)])
    return result_indexes


def sum_price(list_of_km, list_of_rub):
    count = len(list_of_km)
    res = 0
    for i in range(count):
        res += (list_of_rub[i]*list_of_km[i])
    return res


string = list(input().split())
count = int(string[0])
list_of_km = []
list_of_rub = []
fill_lists(string)
indexes_of_km = [x for x in range(1, count + 1)]
indexes_of_rub = [x for x in range(1, count + 1)]

quick_sort(list_of_km, indexes_of_km)
quick_sort(list_of_rub, indexes_of_rub)

list_of_rub.reverse()
indexes_of_rub.reverse()

result_indexes = queue_taxi(indexes_of_km, indexes_of_rub)

price = sum_price(list_of_km, list_of_rub)

print(*result_indexes, sep=' ')
print(price)
