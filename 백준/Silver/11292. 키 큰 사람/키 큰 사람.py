num = int(input())

while (num != 0):
  students = []
  for i in range(num):
    name, ki = input().split()
    student = [name,float(ki)]
    students.append(student)

  students.sort(key= lambda x: x[1], reverse=True)
  
  max_ki = students[0][1]
  answer = ""

  for s in students:
    if(s[1] == max_ki):
      answer += s[0] + " "
    else:
      break
  print(answer)
  num = int(input())