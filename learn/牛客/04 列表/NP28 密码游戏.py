
# 定义数组中i和j位置的元素交换方法
def swap(list, i, j):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp

if __name__ == '__main__':

    # 获取输入的4位数字
    a = int(input())
    # 获取4位整数中的每一位的值
    first = a // 1000
    second = a // 100 - first * 10
    third = a // 10 - first * 100 - second * 10
    fourth = a - 1000 * first - 100 * second - 10 * third
    # 创建临时数组arr，存储每一位的数值
    arr = [first, second, third, fourth]
    # 使用for循环对每一位的数值进行“加上3再除以9的余数代替该位数字”的操作
    for i in range(len(arr)):
        arr[i] = str((arr[i] + 3) % 9)


    # 将第1位和第3位数字交换
    swap(arr, 0, 2)
    # 将第2位和第4位数字交换
    swap(arr, 1, 3)
    # 使用字符串数组的join方法，完成数组转换为字符串的操作
    print(''.join(arr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
