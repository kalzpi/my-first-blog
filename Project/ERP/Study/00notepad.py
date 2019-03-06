import numpy

raw_data = open("Data/Test/test_data.txt", 'r')

data_matrix = raw_data.read()

print(data_matrix)

raw_data.close()
