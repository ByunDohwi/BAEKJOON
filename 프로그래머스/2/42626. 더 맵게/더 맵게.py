import heapq

def solution(scoville, K):
    mix = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        newScov = first+second*2
        heapq.heappush(scoville, newScov)
        mix += 1
        
    return mix