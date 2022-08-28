
def find_max(array):
    max = 0
    for i in array:
        if i > max:
            max = i
    return(max)

def find_max_recursive(array,i):
    if i == len(array) - 1:
        return array[i]
    current_value = array[i]
    max_in_array = find_max_recursive(array,i+1)
    max_array = max(current_value,max_in_array)
    return max_array




if __name__ == '__main__':
    array = [5,76,12,43,6]
    # max = find_max(array)
    # print(max)

    # max = find_max_recursive(array,0)
    # print(max)








