def swap(array, i, j):
    swappe = array[i]
    array[i] = array[j]
    array[j] = swappe


def bubble_sort(before):
    for i in range(len(before)):
        for j in range(len(before)):
            if before[i] < before[j]:
                swap(before, i, j)
    return before


def minimum(before, k):
    array = before[k:]
    mi_idx, mi = 0, array[0]
    for j, e in enumerate(array):
        if e < mi:
            mi = e
            mi_idx = j
    return k + mi_idx, mi


def selection_sort(before):
    for i in range(len(before)):
        mi_idx, mi = minimum(before, i)
        if mi < before[i]:
            swap(before, mi_idx, i)
    return before


def select_pivot(l, r):
    return l + (r - l) // 2


def divide_array(array, l, r):
    pivot_idx = select_pivot(l, r)
    e = array[pivot_idx]
    swap(array, pivot_idx, r)

    current_idx = l
    for i in range(l, r):
        if array[i] < e:
            swap(array, i, current_idx)
            current_idx += 1
    swap(array, current_idx, r)
    return current_idx


def quick_sort(before, l, r):
    if l < r:
        i = divide_array(before, l, r)
        quick_sort(before, l, i - 1)
        quick_sort(before, i + 1, r)
    return before


def qsort(before):
    return quick_sort(before, 0, len(before) - 1)

