word = input()
password = input()

MOD = 900528
answer = 0
mmap = dict()
word_len = len(word)
for idx, key in enumerate(word):
  if not key in mmap:
    mmap[key] = idx

for i, password_word in enumerate(password):
  word_idx = mmap[password_word]+1
  power = len(password)-i-1

  if word_len == 0:
    answer += (mmap[password_word]+1)% MOD
  else:
    answer = (answer + (word_idx * pow(word_len, power, MOD)) % MOD) % MOD

print(answer)
