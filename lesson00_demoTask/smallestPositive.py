def solution(A):
    A.sort()
    smallestPositiveNumber = 1
    for n in A:
        if n == smallestPositiveNumber:
            smallestPositiveNumber += 1

    return smallestPositiveNumber

result = solution([1, 3, 6, 4, 1, 2])
print(result)
