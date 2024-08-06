
if __name__ == '__main__':

    str = input()
    list = []

    str = str.split(' ')
    for i in range(len(str)):
        list.append(str[i])

    list.pop(0)
    print(list)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
