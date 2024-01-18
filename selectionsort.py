def findSmallest(arr)->int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
      if arr[i] < smallest:
        smallest = arr[i]
        smallest_index = i
    return smallest_index


def selectionSort(arr):

    newArr = []
    for _ in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5,3,7,8,2]))

