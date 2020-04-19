

def interest (num,rate,month):
    '''

    will show you how much in total every month(include interest)

    '''
    for i in range(1,month+1):
        num+=num*rate/1200
        print('%3d \t %.2f'%(i,num))

if __name__ == '__main__':
    num,rate,month=eval(input())
    print('%s \t %s'%('Month','Amount'))
    interest(num,rate,month)