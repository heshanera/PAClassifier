import csv
import numpy
from preprocessor import *

input_vector_size = 9
weight_vector = numpy.array([0] * input_vector_size)
data = []
data_size = 0;
predictions_arr = []
C = 1
training_portion = 2/3
testing_portion = 1/3
correct_train_data = 0
correct_train_data_arr = []

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
        classify(vectors)
        

# test using the adjusted weights
# testing_set: data portion for testing
def test(testing_set):
    global data
    global predictions_arr
    predictions = [0]*2
    test_data_size = int(data_size * testing_set)
    
    with open('../predictions.txt', 'w') as the_file:
        the_file.write('')
    
    for i in range(data_size-test_data_size, data_size):
        vectors = create_vector(data[i],[0],[10])
        result = predict(vectors)
        predictions[result] += 1
    predictions_arr.append(predictions)
        

# classify the value using PA-I 
# vectors: array of the input vector and the target class vector
def classify(vectors):
    global weight_vector
    global C
    
    input_vector = numpy.array(vectors[0])
#    input_vector = input_vector / numpy.linalg.norm(input_vector)
    target_vector = vectors[1]
    
    prediction = target_vector[0] * numpy.dot( weight_vector, input_vector)
    loss = max(0, 1 - prediction)  
    
#    delta = loss/ ((numpy.linalg.norm(input_vector))**2) # PA
    delta = min(C, loss/ ((numpy.linalg.norm(input_vector))**2)) # PA-I
#    delta = loss/ (((numpy.linalg.norm(input_vector))**2) + (1/(2*C))) # PA-II
    
    tmp_var = delta*target_vector[0]
    tmp_vec = [val * tmp_var for val in input_vector]
    weight_vector = weight_vector + tmp_vec
    
    global correct_train_data
    if loss == 0:
#    if prediction > 0:
        correct_train_data += 1
    
    
# predict the class
# vectors: array of the input vector and the target class vector
def predict(vectors):
    global weight_vector
    global C
    
    input_vector = numpy.array(vectors[0])
#    input_vector = input_vector / numpy.linalg.norm(input_vector)
    target_vector = vectors[1]
    
    
    prediction = numpy.dot( weight_vector, input_vector)
    absPrediction = target_vector[0] * prediction
    loss = max(0, 1 - absPrediction)  
    
    ######## writting the predictions to a file ###############
    
#    print()
#    print("id: ", vectors[2][0])
#    print("prediction: " , prediction)
#    print("target class: ", target_vector[0])
    if absPrediction > 0:
        classfiction = 'correct'
    else:
        classfiction = 'incorrect'    
#    print("classification: ", classfiction)
#    print()
    
    with open('../predictions.txt', 'a') as the_file:
        the_file.write("id: " + vectors[2][0] +'\n')
        the_file.write("prediction: " + str(prediction) +'\n')
        the_file.write("target class: " + str(target_vector[0]) +'\n')
        the_file.write("classification: " + str(classfiction) +'\n\n')
    
    ###########################################################
    
    ######## return prediction status (correct or incorrect) ###############
#    if loss == 0:
    if absPrediction > 0:
        return 1 # correct prediction
    else:
        return 0 # incorrect prediction
    

def print_results(trainig_iterations):
    global data_size
    global predictions_arr
    global correct_train_data_arr
    test_data_size = int(data_size*(testing_portion))
    train_data_size = int(data_size*(training_portion))
#    print('data size: ' + str(test_data_size))
#    print('correct: ' + str(predictions[1]))
#    print('incorrect: ' + str(predictions[0]))
#    print('accuracy: ' + "{:.2%}".format(predictions[1]/test_data_size))

#    print("----------------------------------------------------------")
#    print("%s\t%s\t\t%s\t%s" % ('data size', 'correct', 'incorrect', 'accuracy'))
#    print("----------------------------------------------------------")
#    print("%d\t\t%d\t\t%d\t\t%s" % (test_data_size, predictions[1], predictions[0], "{:.2%}".format(predictions[1]/test_data_size)))
#    print("----------------------------------------------------------")
    
    print('Train Data Size: ' + str(train_data_size) + '\n')
    titles = ['Iterations', 'Correct', 'Incorrect','Training']
    
    data = [titles]
    for i, d in enumerate(data):
        line = '| '.join(str(x).ljust(12) for x in d)
        print(line)
        if i == 0:
            print('-' * len(line))
    
    index = 0
    for predictions in predictions_arr:
        data = list(zip(
            [trainig_iterations[index]], 
            [correct_train_data_arr[index]], 
            [(train_data_size*trainig_iterations[index])-correct_train_data_arr[index]], 
            ["{:.2%}".format(correct_train_data_arr[index]/(train_data_size*trainig_iterations[index]))], 
        ))
        index += 1
        for i, d in enumerate(data):
            line = '| '.join(str(x).ljust(12) for x in d)
            print(line)
    
    print('\n\n')
    
    print('Test Data Size: ' + str(test_data_size) + '\n')
    titles = ['Iterations', 'Correct', 'Incorrect', 'Testing']
    
    data = [titles]
    for i, d in enumerate(data):
        line = '| '.join(str(x).ljust(12) for x in d)
        print(line)
        if i == 0:
            print('-' * len(line))
    
    index = 0
    for predictions in predictions_arr:
        data = list(zip(
            [trainig_iterations[index]], 
            [predictions[1]], 
            [predictions[0]],
            ["{:.2%}".format(predictions[1]/test_data_size)]
        ))
        index += 1
        for i, d in enumerate(data):
            line = '| '.join(str(x).ljust(12) for x in d)
            print(line)
    
    
            
def reset_weights():
    global weight_vector
    weight_vector = numpy.array([0] * input_vector_size)
    

def main():
    
    global training_portion
    global testing_portion
    
    global correct_train_data
    global correct_train_data_arr
    
    load_data('../datasets/breast_cancer_wisconsin_dataset.csv')
    
    iterations_arr = [1,2,10]
    for trainig_iterations in iterations_arr:
        for i in range(trainig_iterations):
            train(training_portion) # train using 2/3 data
        test(testing_portion) # test using 1/3 data
        reset_weights()
        correct_train_data_arr.append(correct_train_data)
        correct_train_data = 0
    print_results(iterations_arr)
  
if __name__== "__main__":
  main()
