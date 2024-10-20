import sys
import numpy

def average_inflammation():
	script = sys.argv[0]
	filename = sys.argv[1]
	data = numpy.loadtxt(filename, delimiter=',')
	print('running ', script)
	for row_mean in numpy.mean(data, axis=1):
		print(row_mean)


