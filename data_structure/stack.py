def create_stack():
    stack = []
    return stack

def push_stack(stack, item):
    stack.append(item)
    print("pushed item: ", item)

def check_empty(stack):
    return len(stack) == 0

def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()

if __name__ == '__main__':
    stack = create_stack()
    push_stack(stack, 1)
    push_stack(stack, 2)
    push_stack(stack, 3)

    result = pop(stack)
    print(result)
    result = pop(stack)
    print(result)
    result = pop(stack)
    print(result)
    result = pop(stack)
    print(result)


