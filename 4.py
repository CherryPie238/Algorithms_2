def is_subsequence(a, b):
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1

        j += 1

    return i == len(a)

#сдвигаем указатель i в списке a, если находим совпадающие элементы с b, если i дошел до конца, то все элементы из a были в b