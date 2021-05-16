# Shell sort is an optimization over insertion sort. Insertion sort requires many swaps and comparisons
# if heavy elements are located towards the end of an array. Shell sort will initially sort subarrays that are equal distance apart.
def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i

            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor

        gap = gap // 2



if __name__ == '__main__':
    elements = [21, 38, 29, 56, 5, 25, 15, 11, 32, 9]
    shell_sort(elements)
    print(elements)