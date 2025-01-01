import statistics
n = int(input())
for i in range(n):
    score = list(map(int,input().split()))
    del(score[0])
    mean = statistics.mean(score)
    answer = round(((sum(1 for s in score if s > mean))/len(score))*100,3)
    print(f'{answer}%')