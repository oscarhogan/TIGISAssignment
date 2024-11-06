from matplotlib import pyplot as plt

def read_data(filename):
    """
    Define function read_data which parses data from the plenty.data file and adds it to a pair of dictionaries
    on a line by line basis. The first element from each line is added to the x value dictionary and the remainder
    added to the y.
    """
    x = []  # Opening an empty list called 'x'
    y = []  # Opening an empty list called 'y'
    with open(filename) as inputFile:  
        for line in inputFile:  # Looping through each line in the document
            sep = line.split()  # Splits the line into a list of elements based on blank space
            x.append(float(sep[0]))  # Add the first element of the list to the x dictionary
        
            yv= [float(valu) for valu in sep[1:]]  # Add all remaining elements to list 'yv'
            y.append(yv)  # Add yv values to y list
    
    return x, y  # Return the lists

if __name__ == '__main__':
    x, y = read_data("plenty.data")  

def plotXY(x, y):
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, color = 'white')
    plt.gca().set_facecolor('black')
    plt.title("Assignment Data")
    plt.xlabel("X value")
    plt.ylabel("Y value")
    plt.show() 


    
plotXY(x, y)
  

 
            
