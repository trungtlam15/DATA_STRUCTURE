
def find_fibonacci(n):
    if (n <= 1):
        return n
    return find_fibonacci(n-1)+find_fibonacci(n-2)

def find_fibonacci_ver2(n):
    array = []
    array.append(0)
    array.append(1)

    for i in range(2,n+1):
        array.append(array[i-1] + array[i-2])

    return array[n]

if __name__ == '__main__':
    # result = find_fibonacci(8)
    # print(result)

    print(find_fibonacci_ver2(6))