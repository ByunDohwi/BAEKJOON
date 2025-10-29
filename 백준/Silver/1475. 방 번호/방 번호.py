n = input()
num_list = []

def find_su(a):
  return n.count(a)

for i in range(10):
  num_list.append(find_su(str(i)))

num_list[6] = (num_list[6] + num_list[9])//2 + (num_list[6] + num_list[9])%2
num_list.pop(9)

print(max(num_list))