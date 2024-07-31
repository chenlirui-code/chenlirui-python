
if __name__ == '__main__':

    str = input()
    list = []

    str = str.split(' ')
    for i in range(len(str)):
        if str[i] not in list:
            list.append(int(str[i]))

    print(list)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
