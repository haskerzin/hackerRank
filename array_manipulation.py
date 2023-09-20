
import os

def arrayManipulation(n, queries):
    # import array
    # Write your code here
    array = [0]*n
    
    for x in queries:
        b = min(n, x[1])
        array[x[0]-1:b] = [k + x[2] for k in array[x[0]-1:b]]

    array.sort()
    
    return array[-1]
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()