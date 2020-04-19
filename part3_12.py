

def f_c():
    '''

    to show temperature each 10 gap from 10 F to 250 F transform to C

    '''
    for F in range (10,250,10):
        c=5/9*(F-32)
        print('%-4d %8.2f'%(F,c))

if __name__ == '__main__':
    print('%s %7s' % ('華氏', '攝氏'))
    f_c()