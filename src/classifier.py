import csv
import numpy
from preprocessor import *

input_vector_size = 9
weight_vector = numpy.array([0] * input_vector_size)
data = []
data_size = 0;
predictions = [0]*2
C = 1

# read the CSV file at given path
def load_data(file_path):
    global data
    global data_size
    with open(file_path, "r") as file_object:
        reader = csv.reader(file_object)
        for row in reader:
            data.append(row)
            data_size += 1
        

# train the weights 
# training_set: data portion for trainig
def train(training_set):
    global data
    train_data_size = int(data_size * training_set)
    for i in range(train_data_size):
        vectors = create_vector(data[i],[0],[10])
        predict(vectors)
        

# test using the adjusted weights
# testing_set: data portion for testing
def test(testing_set):
    global data
    test_data_size = int(data_size * testing_set)
    for i in range(data_size-test_data_size, data_size):
        vectors = create_vector(data[i],[0],[10])
        result = predict(vectors)
        predictions[result] += 1
        

# predict the value using PA-I 
# vectors: array of the input vector and the target class vector
def predict(vectors):
    global weight_vector
    global C
    
    input_vector = numpy.array(vectors[0])
    input_vector = input_vector / numpy.linalg.norm(input_vector)
    target_vector = vectors[1]
    
    prediction = target_vector[0] * numpy.dot( weight_vector, input_vector)
    loss = max(0, 1 - prediction)  
    
#    delta = loss/ ((numpy.linalg.norm(input_vector))**2) # PA
    delta = min(C, loss/ ((numpy.linalg.norm(input_vector))**2)) # PA-I
#    delta = loss/ (((numpy.linalg.norm(input_vector))**2) + (1/(2*C))) # PA-II
    
    tmp_var = delta*target_vector[0]
    tmp_vec = [val * tmp_var for val in input_vector]
    weight_vector = weight_vector + tmp_vec
    
    if loss == 0:
        return 1 # correct prediction
    else:
        return 0 # incorrect prediction
    

def print_results():
    global data_size
    test_data_size = int(data_size*(1/3))
#    print('data size: ' + str(test_data_size))
#    print('correct: ' + str(predictions[1]))
#    print('incorrect: ' + str(predictions[0]))
#    print('accuracy: ' + "{:.2%}".format(predictions[1]/test_data_size))

    print("%s\t%s\t\t%s\t%s" % ('data size', 'correct', 'incorrect', 'accuracy'))
    print("---------------------------------------------------------------")
    print("%d\t\t%d\t\t%d\t\t%s" % (test_data_size, predictions[1], predictions[0], "{:.2%}".format(predictions[1]/test_data_size)))


def main():
    load_data('../datasets/breast_cancer_wisconsin_dataset.csv')
    
    for i in range(2):
        train(2/3) # train using 2/3 data
    
    test(1/3) # test using 1/3 data
    print_results()
  
if __name__== "__main__":
  main()
