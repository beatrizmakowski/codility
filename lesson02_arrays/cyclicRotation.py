def solution(A, K):
    if len(A) == 0:
        return A
    lastIndex = len(A) - 1
    for k in range(K):
        A.insert(0, A[lastIndex])
        A.pop()
    return A
