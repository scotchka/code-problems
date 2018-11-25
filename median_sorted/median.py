def middle(start, end):
    half = (end - start) // 2

    if (end - start) % 2 == 1:
        return start + half, start + half
    else:
        return start + half - 1, start + half


def bisect(num, lst, start, end):

    while end - start > 2:
        _, mid = middle(start, end)

        if num <= lst[mid]:
            end = mid
        else:
            start = mid + 1

    if num <= lst[start]:
        return start
    elif end - start == 1 or num <= lst[start + 1]:
        return start + 1
    else:
        return start + 2


def one_median(num, lst, start, end):

    i = bisect(num, lst, start, end)

    if (end - start) % 2 == 1:
        mid, mid = middle(start, end)
        if i < mid:
            return (lst[mid - 1] + lst[mid]) / 2
        elif i in (mid, mid + 1):
            return (num + lst[mid]) / 2
        else:
            return (lst[mid] + lst[mid + 1]) / 2

    else:
        left, right = middle(start, end)
        if i < right:
            return lst[left]
        elif i == right:
            return num
        else:
            return lst[right]


def median(a, b):
    if len(a) > len(b):
        a, b = b, a

    start_a = start_b = 0
    end_a = len(a)
    end_b = len(b)

    while end_a - start_a > 1:
        i_a, j_a = middle(start_a, end_a)
        i_b, j_b = middle(start_b, end_b)

        if a[j_a] < b[i_b]:
            length = j_a - start_a
            start_a += length  # a = a[j:]
            end_b -= length  # b = b[:i + 1]

        elif b[j_b] < a[i_a]:
            length = end_a - (i_a + 1)
            end_a -= length  # a = a[:i + 1]
            start_b += length  # b = b[j:]

        else:
            break

    if end_a - start_a == 1:
        return one_median(a[start_a], b, start_b, end_b)

    i_a, j_a = middle(start_a, end_a)
    i_b, j_b = middle(start_b, end_b)

    if a[i_a] <= b[i_b] <= b[j_b] <= a[j_a]:
        return (b[i_b] + b[j_b]) / 2
    if b[i_b] <= a[i_a] <= a[j_a] <= b[j_b]:
        return (a[i_a] + a[j_a]) / 2

    if a[i_a] <= b[i_b] <= a[j_a] <= b[j_b]:
        return (b[i_b] + a[j_a]) / 2
    if b[i_b] <= a[i_a] <= b[j_b] <= a[j_a]:
        return (a[i_a] + b[j_b]) / 2
