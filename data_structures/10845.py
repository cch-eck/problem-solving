def push(X: int, queue):
    queue.append(X)
    
def pop(queue):
    if empty(queue):
        return -1
    result = queue[0]
    del(queue[0])
    return result

def empty(queue):
    if len(queue)<=0: 
        return 1
    return 0

def size(queue):
    return len(queue)

def front(queue):
    if empty(queue):
        return -1
    return queue[0]

def back(queue):
    if empty(queue):
        return -1
    return queue[-1]

n = int(input())
queue = []
for _ in range(n):
    line = input().split(' ')
    command = line[0]
    match command:
        case "push":
            push(int(line[1]), queue)
        case "front":
            print(front(queue))
        case "back":
            print(back(queue))
        case "size":
            print(size(queue))
        case "empty":
            print(empty(queue))
        case "pop":
            print(pop(queue))
        case default:
            continue