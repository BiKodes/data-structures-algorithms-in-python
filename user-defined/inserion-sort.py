# Insertion sort is a simple sorting algorithm (Very few lines of code) that is best for small lists.
# If your array is very big insertion sort might not be the perfect choice as it performs in O(n^2) time complexity.

def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1

        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1

        elements[j + 1] = anchor

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(elements)
    print(elements)