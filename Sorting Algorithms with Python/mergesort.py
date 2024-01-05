def mergeSort(data):
  if len(data) > 1:
    middle = len(data) // 2
    left, right = data[:middle], data[middle:]
    mergeSort(left)
    mergeSort(right)
    i = j = k = 0
    while (i < len(left)) and (j < len(right)):
      if left[i] < right[j]:
        data[k] = left[i]
        i = i + 1
      else:
        data[k] = right[j]
        j = j + 1
      k = k + 1
    while i < len(left):
      data[k] = left[i]
      i = i + 1
      k = k + 1
    while j < len(right):
      data[k] = right[j]
      j = j + 1
      k = k + 1

data = [8, 7, 6, 5, 4, 3, 2, 1]
mergeSort(data)
print(data)
