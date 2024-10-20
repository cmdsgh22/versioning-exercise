import sys
import numpy

def average_inflammation():
	script = sys.argv[0]
	for filename in sys.argv[1:]:
		print('running ', script, 'for ', filename)
		data = numpy.loadtxt(filename, delimiter=',')
		for row_mean in numpy.mean(data, axis=1):
			print(row_mean)

if __name__ == '__main__':
	average_inflammation()
