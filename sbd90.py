#Recursive Insertion Sort

def ins_sort(arr, n):
    if n <= 1:
        return
    ins_sort(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last

a = [-7, 11, 6, 0, -3, 5, 10, 2]
ins_sort(a, len(a))
print(a)