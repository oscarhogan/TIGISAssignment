import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
import matplotlib as mpl

def rundata(filename):
    """
    Define the function rundata which parses data from the natural neighbourhoods text
    file using the argument 'filename', extracting the neighbourhood name which is used
    as a key and a set of xy coordinates. Each dictionary is added to a list
    """
    edinburgh = {}  # Opening an empty dictionary
    with open(filename) as inputFile:
        name = ""  # Create an empty string to store neighbourhood name

        for line in inputFile:  # Loop through each line of the file
            line = line.strip()  # Remove trailing and starting whitespace

            if line.startswith('#'):  # Skip metadata lines starting with '#'
                continue

            if line:  # Skip empty lines
                if line[0].isalpha():  # If the line starts with a letter it is a name
                    name = line
                    edinburgh[name] = [] # Create a list within the dictionary for the neighbourhood
                elif line.startswith('['):
                    # If the line starts with '[', it contains data in the incorrect format
                    line = line.strip('[]')  # Remove the square brackets
                    coords = line.split('), (')  # Coordinate pairs separated based on '), ('

                    for pair in coords:  # Loop through the coordinate pairings
                        pair = pair.strip('()')  # Isolates the numeric information
                        koords = pair.split(', ')  # Split into individual tuple elements
                        xdata = float(koords[0])  # First element converted to float
                        ydata = float(koords[1])  # Second element converted to float
                        edinburgh[name].append((xdata, ydata))  # Add to the dictionary

                elif line.startswith('('):  # If the line starts with '(', it forms a coordinate pair of well-formatted points
                    qoords = line.strip('()').split(', ')  # Remove the brackets and split into tuple elements
                    xdata = float(qoords[0])  # Convert to float
                    ydata = float(qoords[1])  # Convert to float
                    edinburgh[name].append((xdata, ydata))  # Add to the list

    return edinburgh

mpl.rcParams['font.family'] = 'serif'
   
def plot_data(data):
    """
    Function to plot the neighbourhood data on a map using Cartopy with an OpenStreetMap basemap.
    """
    fig = plt.figure(figsize=(8, 10), dpi=150)

    fig.patch.set_facecolor('lightgray')    

    osgb = ccrs.OSGB(approx=True)

    geo_axes = plt.axes(projection=osgb)
    geo_axes.set_extent((305000, 336000, 658000, 680000), crs=osgb)  # Set the extent for Edinburgh
  
    osm = cimgt.OSM()  # OpenStreetMap basemap
    geo_axes.add_image(osm, 14)  # Add OpenStreetMap tile layer at zoom level 14

    # Plot neighbourhood boundaries using lines (no polygons)
    for name, coords in data.items():
        x, y = zip(*coords)  # Unpack the coordinates
        geo_axes.fill(x, y, color='lightblue', alpha=0.5)
        geo_axes.plot(x, y, linestyle='-', label=name, color='darkblue', linewidth=0.8)  # Plot the neighbourhood boundaries

    # Set ticks on x and y axes (optional for better visual)
    x_ticks = range(305000, 336000, 2000)
    y_ticks = range(658000, 683000, 2000)
    
    geo_axes.set_xticklabels(list(x_ticks), rotation=90)
    geo_axes.set_yticklabels(list(y_ticks))

    geo_axes.xaxis.set_tick_params(labelsize=8)
    geo_axes.yaxis.set_tick_params(labelsize=8)
    
    # Show the plot with the neighbourhood boundaries and OpenStreetMap tiles
    plt.title("Neighbourhoods of Edinburgh", fontsize=20, color='darkblue')
    plt.show()

if __name__ == '__main__':
    # Read data from the file and store it in the `edinburgh` dictionary
    edinburgh = rundata("natural_neighbourhoods.dat")
    print(edinburgh)  # Print the parsed data (for debugging purposes)
    plot_data(edinburgh)
