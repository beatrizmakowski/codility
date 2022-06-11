def solution(N):
    # Convert N to binary binaryArray
    binaryN = bin(N).replace("0b", "")
    binaryArray = list(binaryN)

    # Find the index of each ocurrence of the number 1
    indexesOfOnes = []
    for i in range(len(binaryArray)):
        if binaryArray[i] == '1':
            indexesOfOnes.append(i)
    indexesOfOnes.reverse()

    # Binary gaps are not possible with less than 2 ocurrences of the number 1
    if len(indexesOfOnes) <= 1:
        return 0
    
    # Calculate the size of each binary gap and return the max value
    gaps = []
    for i in range(len(indexesOfOnes) - 1):
        gaps.append( indexesOfOnes[i] - indexesOfOnes[i + 1] - 1)

    return max(gaps)