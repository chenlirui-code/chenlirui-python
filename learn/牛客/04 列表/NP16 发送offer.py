
if __name__ == '__main__':

    offer_list = ['Allen', 'Tom']
    for i in offer_list:
        print('{}, you have passed our interview and will '
              'soon become a member of our company.'.format(i))

    offer_list.remove('Tom')
    offer_list.append('Andy')
    for j in offer_list:
        print('{}, welcome to join us!'.format(j))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
