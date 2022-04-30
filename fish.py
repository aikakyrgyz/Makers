def solution(A, B):
    # write your code in Python 3.6

    size = []
    stream = []

    for i in range(len(A)):
        if len(stream)!=0 and stream[len(stream)-1]== 1 and B[i] == 0:
            if size[len(size)-1] > A[i]:
                pass        
            else:
                while len(stream)!= 0:
                    if stream[len(stream)-1] == 0:
                        size.append(A[i])
                        stream.append(B[i])
                        break
                    if size[len(size)-1] > A[i]:
                        break
                    else:
                        size.pop()
                        stream.pop()
                if len(stream) == 0:
                    stream.append(B[i])
                    size.append(A[i])                

        else:
            size.append(A[i])
            stream.append(B[i])
        
    return len(size)  

A = [43,36,21,19,39,112]
B = [1,1,0,0,1,1]

print(solution(A, B))
