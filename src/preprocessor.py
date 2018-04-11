# convert a number strings into numbers
# convert other input into 0
def to_number(data):
    if type(data) != 'int':
        try:
            return int(data)
        except:
            return 0
            
        
# create input vector and target vector
# ini_vector: initial data
# exclude: array index of the columns that should be excluded to create input
# target: array index of the target class
def create_vector(ini_vector,exclude,target):
    refac_vector = []
    target_vector = []
    exclude_vector = []
    if (len(exclude) == 0 and len(target) == 0):
        for value in ini_vector:
            int_value = to_number(value)
            refac_vector.append(int_value)
    else:
        i = -1
        for value in ini_vector:
            i += 1
            if i in exclude:
                exclude_vector.append(value)
            elif i in target:
                if value == '2':
                    target_vector.append(-1)
                elif value == '4':
                    target_vector.append(1)
            else:
                int_value = to_number(value)
                refac_vector.append(int_value)
    return [refac_vector, target_vector, exclude_vector]
        
        
        
    
    
    
    