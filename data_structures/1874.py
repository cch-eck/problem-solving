def stack_test():
    n = int(input())
    seq = [int(input()) for _ in range(n)]
    stack = []
    answer = []
    current = 1
    
    for num in seq:
        while num >= current:
            stack.append(current)
            answer.append('+')
            current+=1
            if current>n+1:
                return 0
        if stack[-1] == num:
            stack.pop()
            answer.append('-')
        else:
            print("NO")
            return []
    return answer

answer = stack_test()
if answer!=[]:
    # print(answer)
    print('\n'.join(answer))