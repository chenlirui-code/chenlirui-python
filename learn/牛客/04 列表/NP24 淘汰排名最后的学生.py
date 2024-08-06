
if __name__ == '__main__':

    str = input()

    list = []
    str = str.split(' ')
    for i in range(len(str)):
        list.append(str[i])

    # print(list)
    len = len(list)

    for i in range(3):  # 相当于 for i in [0, 1, 2, 3, 4]
        list.pop()


    print(list)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
