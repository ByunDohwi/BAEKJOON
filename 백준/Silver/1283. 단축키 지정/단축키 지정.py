N = int(input())
단축키 = set(" ")
words = []

def 단축키_생성(스트링):
  if 스트링.upper() in 단축키:
    return False
  else:
    단축키.add(스트링.upper())
    return True


for i in range(N):
  words.append(input())

for word in words:
  answer = ""
  word_list = word.split()
  flag = False
  for 단어 in word_list:
    if not flag and 단축키_생성(단어[0]):
      answer += "["+단어[0]+"]"+단어[1:]+" "
      flag = True
    else:
      answer += 단어+" "
  if flag:
    print(answer)
  else:
    answer = ""
    for idx, 글자 in enumerate(word):
      if 단축키_생성(글자):
        answer += "["+글자+"]"+word[(idx+1):]
        break
      else:
        answer += 글자
    print(answer)
  