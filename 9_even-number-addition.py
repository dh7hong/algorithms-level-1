def solution(n):
    answer = 0
    for i in evens(n):
        answer += i
    return answer

def evens(n):
    evens = []
    for i in range(1, n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens

print(evens(10)) # 30
print(evens(4)) # 6

print(solution(10)) # 30
print(solution(4)) # 6


def solution2(n):
    answer = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            answer += i
    return answer