class Stack:
    def __init__(self):
        self.stack = []

    def push_stack(self, item):
        self.stack.append(item)
        # print("pushed item: ", item)

    def check_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if (self.check_empty()):
            return "stack is empty"
        return self.stack.pop()

if __name__ == '__main__':
    stack = Stack()
    # stack.push_stack(1)
    # stack.push_stack(2)
    # stack.push_stack(3)
    # result = stack.pop()
    # print(result)
    # result = stack.pop()
    # print(result)
    # result = stack.pop()
    # print(result)
    # result = stack.pop()
    # print(result)

    is_valid = True
    string = "(())"
    for i in string:
        if i == "(":
            stack.push_stack(i)
        else:
            last_value = stack.pop()
            if last_value == "(":
                continue
            else:
                is_valid = False
                break

    print(is_valid)







