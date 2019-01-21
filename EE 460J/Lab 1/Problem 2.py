import numpy
import matplotlib

n = 1000
totalsum = []

for number in range(1000):
    sum = 0
    array = numpy.random.binomial(1, .5, n)
    for i in range(len(array)):
        if array[i] == 0:
            array[i] = -1
        sum += array[i]
    sum /= n
    totalsum.append(sum)

matplotlib.pyplot.hist(totalsum)
