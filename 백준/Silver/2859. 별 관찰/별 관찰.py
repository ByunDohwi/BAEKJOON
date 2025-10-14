#[0] - h , [1] - m
days = ["Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def make_m(m):
  if m == 0:
    return "00"
  elif m < 10:
    return "0"+str(m)
  else:
    return str(m)

def make_h(h):
  if h < 10:
    return "0"+str(h)
  else:
    return str(h)

star1_time = list(map(int,input().split(":")))
star2_time = list(map(int,input().split(":")))
star1_cycle = list(map(int,input().split(":")))
star2_cycle = list(map(int,input().split(":")))

while (24*100*60 > star1_time[0] or 24*100*60 > star2_time[0]):
  if star1_time[0]+(star1_time[1]/100) == star2_time[0]+(star2_time[1]/100):
    print(days[(star2_time[0]//24)%7])
    print(make_m(star2_time[0]%24)+":"+make_m(star2_time[1]))
    exit()
  elif star1_time[0]+(star1_time[1]/100) > star2_time[0]+(star2_time[1]/100):
    star2_time[0] += star2_cycle[0]
    star2_time[1] += star2_cycle[1]
    if star2_time[1] >= 60:
      star2_time[0] += 1
      star2_time[1] -= 60
  else:
    star1_time[0] += star1_cycle[0]
    star1_time[1] += star1_cycle[1]
    if star1_time[1] >= 60:
      star1_time[0] += 1
      star1_time[1] -= 60
print("Never")