def count_by_range(array, Lv, Rv):
    n = len(array)
    
    start = 0
    end = n
    
    while start < end:
        mid = (start + end) // 2
        if array[mid] <= Lv:
            start = mid + 1
        else:
            end = mid
        Li = start
        
        start = 0
        end = n
        
        mid = (start + end) // 2
        if array[mid] <= Rv:
            start = mid + 1
        else:
            end = mid
        Ri = start
        
    return Ri - Li

def solution(words, queries):
    answer = []
    
    word_list = [[] for _ in range(10001)]
    reversed_word_list = [[] for _ in range(10001)]
    
    for word in words:
        word_list[len(word)].append(word)
        reversed_word_list[len(word)].append(word[::-1])
    
    for query in queries:
        if query[0] != '?':
            count = answer.append(count_by_range(word_list[len(query)], query.replace('?', 'a'), query.replace('?', 'z')))
        else:
            count = answer.append(count_by_range(reversed_word_list[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')))
        
        answer.append(count)
    
    return answer