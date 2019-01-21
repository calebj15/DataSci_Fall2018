import numpy
import matplotlib

array1 = numpy.random.normal(-10,5,1000)
array2 = numpy.random.normal(10,5,1000)
array3 = []

for x in range (0, len(array1)):
    array3.append(array1[x] + array2[x])

matplotlib.pyplot.hist(array3)
