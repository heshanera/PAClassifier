import csv

# convert a number strings into numbers
# convert other input into 0
def to_number(data):
    if type(data) != 'int':
        try:
            return int(data)
        except:
            return 0


# read the CSV file at given path
def read_csv_file(file_path):
    with open(file_path, "r") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            print(" ".join(row))
            
        
# exclude the columns in the argument array and return input vector
def create_input_vector(exclude, row):
    ini_vector = row.split(",")
    refac_vector = []
    if len(exclude) == 0:
        for value in ini_vector:
            int_value = to_number(value)
            refac_vector.append(int_value)
    else:
        i = -1
        for value in ini_vector:
            i += 1
            if i in exclude:
                continue
            else:
                int_value = to_number(value)
                refac_vector.append(int_value)
    return refac_vector
        
        
        
    
    
    
    