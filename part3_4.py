
def doublefive(num):
    '''

    sum 1 to num all of the multiple of 5.

    '''
    ans = 0
    for i in range(1,num+1):
        if i % 5 == 0 :
            ans += i
    return ans

if __name__ == '__main__':
    num=eval(input())
    doublefive(num)
    print(doublefive(num))
