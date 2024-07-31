
if __name__ == '__main__':

    str = input()
    str2 = input()
    # print(str2)

    list = []
    str = str.split(' ')
    for i in range(len(str)):
        list.append(str[i])

    # print(list)
    if str2 in list:
        # print('YES')
        list.remove(str2)
    print(list)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
