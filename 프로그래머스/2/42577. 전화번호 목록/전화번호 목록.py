def solution(phone_book):
    sseett = set([])
    phone_book.sort(key=len, reverse=True)

    for phone_num in phone_book: 
        if phone_num in sseett: 
            return False
        for idx in  range(len(phone_num)):
            sseett.add(phone_num[:idx])

    return True