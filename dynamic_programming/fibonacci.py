
def find_fibonacci(n):
    if (n <= 1):
        return n
    return find_fibonacci(n-1)+find_fibonacci(n-2)




if __name__ == '__main__':
    result = find_fibonacci(8)
    print(result)