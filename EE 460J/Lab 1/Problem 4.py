import numpy

mean = [-5, 5]
cov = [[20, .8], [.8, 30]]

array = numpy.random.multivariate_normal(mean, cov, 10000)

sum1 = 0
sum2 = 0
for value in array:
    sum1 += value[0]
    sum2 += value[1]

mean1 = sum1/10000
mean2 = sum2/10000

corrx = 0
corrxy = 0
corry = 0
for value in array:
    corrx += (value[0] - mean1) ** 2
    corrxy += ((value[0] - mean1) * (value[1] - mean2))
    corry += (value[1] - mean2) ** 2
corrx /= 9999
corrxy /= 9999
corry /= 9999

covariance = [[corrx, corrxy], [corrxy, corry]]

print (mean1)
print (mean2)
print (covariance)
