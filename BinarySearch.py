def binary_search(lst: object, item: object) -> object:
    low = 0
    high = len(lst)-1
    while low <= high:
      mid = (low+high)//2
      guess = lst[mid]

      if guess == item:
          return mid
      elif guess > item:
          high = mid - 1
      else:
          low = mid + 1

    return None




