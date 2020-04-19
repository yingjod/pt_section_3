
def tuition_(tuition):
    '''

    after how many year you will pay more than double price compare with first year for study fee

    '''
    year = 0
    tuitionD = tuition * 2
    while tuition<tuitionD:
        year += 1
        tuition *= 1.03
        print('#%d year: %.2f'%(year,tuition))
    print('tuition will be doubled in %d year'%(year))


if __name__ == '__main__':
    tuition=eval(input())
    tuition_(tuition)
