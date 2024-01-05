def quickSort(data, start, end):
  if start < end:
    position = partition(data, start, end)
    quickSort(data, start, position - 1)
    quickSort(data, position + 1, end)

def partition(data, start, end):
  pivot = data[start]
  left = start + 1
  right = end
  flag = False
  while not flag:
    while (left <= right) and (data[left] <= pivot):
      left = left + 1
    while (right >= left) and (data[right] >= pivot):
      right = right - 1
    if right < left:
      flag = True
    else:
      memory = data[left]
      data[left] = data[right]
      data[right] = memory
  memory = data[start]
  data[start] = data[right]
  data[right] = memory
  return right


data = [8, 7, 6, 5, 4, 3, 2, 1]
quickSort(data, 0, len(data) - 1)
print(data)
