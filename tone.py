"""
This module includes a function which receives a data file with a series of x and y values -
with there being 10 y values for each x value - and plots them in a graph.
"""

from matplotlib import pyplot as plt

def read_data(filename):
    """
    Define function read_data which parses data from the plenty.data file and adds it
    to a pair of lists on a line by line basis. The first element from each line
    is added to the x value list and the remainder added to the y list.

    Args:
        filename: The name of the file ("plenty.data")

    Returns:
        A tuple containing two lists:
        - The first list contains x values.
        - The second list is a list of lists, where each inner list 
            contains 10 y values corresponding to each x value.
    """
    x_vals = []  # List to store x values
    y_vals = []  # List to store y values (a list of lists)

    with open(filename) as input_file:
        for line in input_file:  # Looping through each line in the document
            sep = line.split()  # Split the line into a list of elements based on space
            x_vals.append(float(sep[0]))  # Add the first element of the list to x_vals
            yv = [float(valu) for valu in sep[1:]]  # Convert the rest to float and store in yv
            y_vals.append(yv)  # Append the list of y values to y_vals

    return x_vals, y_vals  # Return the lists

if __name__ == '__main__':
    x_vals, y_vals = read_data("plenty.data")  # Read data from the file

    plt.figure(figsize=(10, 10))
    plt.plot(x_vals, y_vals, color='white')
    plt.gca().set_facecolor('black')
    plt.title("Assignment Data", size=20, color='white')
    plt.xlabel("X value", color='white')
    plt.ylabel("Y value", color='white')
    plt.show()
    # Specifying figure characteristics 

 
