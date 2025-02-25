# def solution(numbers):
#     return sum(numbers) / len(numbers)

def solution(numbers):
    
    answer = 0
    for number in numbers:
        answer += number
        
    return answer / len(numbers)

print(solution([1, 2, 3, 4])) # 2.5