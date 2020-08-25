import numpy

def my_sum(my_arr):
    #The sum tool returns the sum of array elements over a given axis.
    #'0' means vertically down
    #'1' means vertically across
    return numpy.sum(my_arr, axis = 0)

def product(my_arr):
    #The prod tool returns the product of array elements over a given axis.
    #By default, the axis value is None. Therefore, it performs the product over all the dimensions of the input array.
    print(numpy.prod(my_arr,axis = None))

if __name__ == '__main__':
    row, column = map(int, input().split())
    #Taking 2D input
    my_arr = numpy.array([input().strip().split() for _ in range(row)],int)
    product(my_sum(my_arr))
