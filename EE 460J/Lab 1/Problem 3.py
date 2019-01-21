import numpy
import matplotlib
import math

array = numpy.random.normal(0,5,25000)

sum = 0
for value in array:
    sum += value
mean = sum/len(array)

newarray = []
for value in array:
    newarray.append(value)

sum = 0
for i in range(len(array)):
    newarray[i] = (newarray[i] - mean) ** 2
    sum += newarray[i]
std = math.sqrt(sum/len(array))


print("Mean: " + str(mean))
print("Std:" + str(std))

matplotlib.pyplot.hist(array)
