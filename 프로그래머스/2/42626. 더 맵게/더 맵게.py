import heapq
def solution(scoville, K):
    answer = 0
    a = 1
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        if scoville[0] >= K:
            return answer
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        assem = first + second * 2
        heapq.heappush(scoville, assem)
        answer += 1

    return answer if scoville[0] >= K else -1