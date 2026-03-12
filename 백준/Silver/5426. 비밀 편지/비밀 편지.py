def find_square(len):
  for i in range(1,101):
    if len // i == i:
      return i


N = int(input())

for i in range(N):
  letter = input()
  letter_square = find_square(len(letter))
  for j in range(letter_square-1,-1,-1):
    for k in range(j, len(letter), letter_square):
      print(letter[k],end="")
  print("")