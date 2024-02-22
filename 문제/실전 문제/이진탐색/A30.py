# def count_by_range(array, left_value, right_value):
#     left_index = 0
#     right_index = len(array) - 1

#     while left_index <= right_index:
#         mid_index = (left_index + right_index) // 2

#         if array[mid_index] > right_value:
#             right_index = mid_index - 1
#         elif array[mid_index] < left_value:
#             left_index = mid_index + 1
#         else:
#             break
#     else:  # while 루프가 종료되면 실행
#         return 0

#     left_count = 0
#     right_count = 0

#     # 왼쪽 범위의 개수 구하기
#     for i in range(mid_index, -1, -1):
#         if array[i] >= left_value:
#             left_count += 1
#         else:
#             break

#     # 오른쪽 범위의 개수 구하기
#     for i in range(mid_index + 1, len(array)):
#         if array[i] <= right_value:
#             right_count += 1
#         else:
#             break

#     return right_count + left_count

def count_by_range(array, left_value, right_value):
    n = len(array)

    # 범위의 시작 인덱스 찾기
    start = 0
    end = n
    while start < end:
        mid = (start + end) // 2
        if array[mid] <= left_value:
            start = mid + 1
        else:
            end = mid
    left_index = start

    # 범위의 끝 인덱스 찾기
    start = 0
    end = n
    while start < end:
        mid = (start + end) // 2
        if array[mid] <= right_value:
            start = mid + 1
        else:
            end = mid
    right_index = start

    # 범위 내의 요소 수 반환
    return right_index - left_index

def solution(words, queries):
    answer = []

    # 길이별 단어 리스트 생성
    word_list = [[] for _ in range(10001)]
    reversed_word_list = [[] for _ in range(10001)]

    for word in words:
        word_list[len(word)].append(word)
        reversed_word_list[len(word)].append(word[::-1])

    # 이진 탐색을 위한 정렬
    for i in range(10001):
        word_list[i].sort()
        reversed_word_list[i].sort()

    # 쿼리 처리
    for query in queries:
        if query[0] != '?':
            count = count_by_range(word_list[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else:
            count = count_by_range(reversed_word_list[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))

        answer.append(count)

    return answer
