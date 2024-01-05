def bubbleSort(data):
  size = len(data)
  for i in range (0, size, 1):
    for j in range (0, size - 1, 1):
      if data[j] > data[j + 1]:
        memory = data[j]
        data [j] = data[j + 1]
        data[j + 1] = memory


data = [5, 4, 3, 2, 1]
bubbleSort(data)
print(data)
