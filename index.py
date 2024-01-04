def decode(message_file):
  file = open(message_file, "r")

  line = file.readline()
  arr = []

  while line:
    inArr = line.rstrip().split(" ")
    arr.append(inArr)
    line = file.readline()

  arr.sort(key=lambda inArr : inArr[0])

  level = 1
  subsets = []
  while len(arr) != 0:
    subsets.append(arr[0:level])
    arr = arr[level:]
    level += 1

  finalWord = ''
  for sub in subsets:
    finalWord += sub[-1][1] + ' '

  file.close()
  return finalWord.strip()

print(decode("data.txt"))
