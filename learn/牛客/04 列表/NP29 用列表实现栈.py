
if __name__ == '__main__':

    num = eval(input())
    stack = [1, 2, 3, 4, 5]
    for _ in range(2):
        stack.pop()
        print(stack)
    stack.append(num)
    print(stack)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
