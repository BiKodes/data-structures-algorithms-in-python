# Merge sort is a sorting algorithm that gives time complexity of O(nlogn) and thus performs better than insertion sort,
# bubble sort.

def merge_two_sorted_lists(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1

        else:
            sorted_list.append(b[j])
            j += 1

    while i < len_a:
        sorted_list.append(a[i])
        i += 1

    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list


if __name__=='__main__':
    a = [5, 8, 12, 56, 89, 100]
    b = [7, 9, 45, 51]

    print(merge_two_sorted_lists(a,b))