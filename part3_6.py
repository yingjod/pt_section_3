
def checki(n):
    '''

    Multiple all number  from 1 to n

    '''
    result = 1
    for i in range (1,n+1):
        result *= i
    return result

if __name__ == '__main__':
    n = eval(input())
    checki(n)
    print(checki(n))