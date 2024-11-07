"""
This module includes a function which receives coordinate data
associated with neighbourhoods in Edinburgh. It then removes metadata
and cleans lines of a different format. The data gives and index values
to each neighbourhood to be used for plotting before assigning values
to a structure consisting of a dictionary with the name key value and
a nested dictionary containing the index and cooridnate values.

    An additional function creates a cartogrpahical output using
    functions from several geospatial libraries including cartpy
    and shapely, standardising elements for using wihtin matplotlib.
"""

import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as mpl_polygon
from shapely.geometry import Polygon

def rundata(filename):
    """
    Function to parse the neighbourhood data from the file and return
    it as a dictionary. Each neighbourhood name is a key and the corresponding
    coordinates are in a list of tuples.

    Args:
        The name of the file containing neighbourhood data.

    Returns:
        dict: A dictionary with neighbourhood names as keys and coordinates as values.
    """
    edinburgh = {}  # Initialize an empty dictionary named Edinburgh
    index = 1  # Initialize an index which proceeds from '1'

    with open(filename) as inputfile:
        name = ""  # Create an empty string to store neighbourhood name for proccesing

        for line in inputfile:  # Loop through each line of the file
            line = line.strip()  # Remove trailing and starting whitespace

            if line.startswith('#'):  # Skip metadata lines starting with '#'
                continue

            if line:  # Skip empty lines
                if line[0].isalpha():  # If the line starts with a letter, it's a district name
                    name = line
                    edinburgh[name] = {'index': index, 'coordinates': []}
                    # Creates an entry in the edinburgh dictionary. Name is key
                    # Contains dictionary with index number and coordinates

                    index += 1  # For each instance of name line, index increases by 1
                elif line.startswith('['):
                    # If the line starts with '[', it contains data in the incorrect format
                    line = line.strip('[]')  # Remove the square brackets
                    coords = line.split('), (')  # Coordinate pairs separated based on '), ('

                    for pair in coords:  # Loop through the coordinate pairings
                        pair = pair.strip('()')  # Isolates the numeric information
                        try:
                            koords = pair.split(', ')  # Split into individual tuple elements
                            xdata = float(koords[0])  # First element converted to float
                            ydata = float(koords[1])  # Second element converted to float
                            edinburgh[name]['coordinates'].append((xdata, ydata))
                            # Add to the dictionary
                        except ValueError:
                            print(f"failed to convert {pair} to float")  #Error if line cannot
                            #be converted; in the case of non numeric figures for instance.
                            continue

                elif line.startswith('('):  # If the line starts with '(', proceed
                    try:
                        qoords = line.strip('()').split(', ')
                        # Remove the brackets and split into tuple elements
                        xdata = float(qoords[0])  # Convert to float
                        ydata = float(qoords[1])  # Convert to float
                        edinburgh[name]['coordinates'].append((xdata, ydata))  # Add to the list
                    except ValueError:
                        print(f"failed to convert {line} to float")
                        # Error if line cannot be converted to float
                        continue

    return edinburgh

mpl.rcParams['font.family'] = 'serif'  # Set a more elegant font for Matplotlib plots

def plot_data(data):
    """
    Function plots the neighbourhood data, assigning each area a polygon based on the
    coordinate extents specified in the coord list of tuples. This is done using the
    Shapely Polygon feature. The figuresize and bounding box is specified to allow the
    positioning of a key which makes reference to the index included in the 'rundata'
    function. The centroid of each polygon is calculated such that the index value is
    positioned within each polygon extent as a label, beng referenced within the legend.

    Args:
        The data dictionary as specified by the rundata function

    Returns:
        A matplotlib figure output featuring an imported OSM tile as background and
        polygons demonstrating neighbourhood extent. A figure will allow translation
        between the index and neighbourhoods.
    """

    fig = plt.figure(figsize=(12, 14), dpi=150)
    # Define fig as a plt figure with large extent and high resolution
    fig.patch.set_facecolor('lightgray')
    # Set the background sheet colour as grey

    osgb = ccrs.OSGB(approx=True)
    # Define the coordinate reference systsem as ESPG:27700

    geo_axes = plt.axes(projection=osgb)
    # Affirm the coordinate reference system within the plot

    geo_axes.set_position([-0.14, 0.1, 0.85, 0.8])
    # Setting the position of the plot to the far left

    osm = cimgt.OSM()  # Define the imported tileset as Open Street Map
    geo_axes.add_image(osm, 14)  # Adding the OSM background tile

    for name, data in data.items():
        # Loop over each item in the dictionary to plot as Shapely polygons
        coords = data['coordinates']
        # object coords extracts coordinate list from each nested dictionary
        if coords:  # If empty skip
            polygon = Polygon(coords)
            # Use Shapely polygon function to create polygons from coords

            poly = mpl_polygon(list(polygon.exterior.coords),
                               edgecolor='darkblue', facecolor='darkblue', alpha=0.6)
            # Create mpl polygon object from the outermost bounds of the Shapely polygon

            geo_axes.add_patch(poly)
            # List conversion required to fir format required by matplotlib

            geo_axes.plot(*polygon.exterior.xy, linestyle='-',
                          color='lightblue', linewidth=0.8, label=f"{data['index']}. {name}")
            # Plotting data in legible style with the label including index and name values

            index = data['index']
            # Affirming the index is the one specified within the datastructure ready for map labels

            centroid = polygon.centroid  # Defining centroid locaion using centroid function
            geo_axes.text(centroid.x, centroid.y, f"{index}", fontsize=5,
                          ha='center', va='center', color='white', fontweight='bold')
            # Position the index at the centroid location in nice font style

    plt.title("Districts of Edinburgh", fontsize=20, color='darkblue', fontweight='bold')
    # Creating a legible title

    plt.legend(loc='center left', bbox_to_anchor=(1.12, 0.5), title="Districts", ncol=3, fontsize=5)
    # Positioning legend to the right of the map using bbox_to_anchor, 3 columns for readability

    plt.show()  # Display plot

if __name__ == '__main__':

    edinburgh_run = rundata("natural_neighbourhoods.dat")
    plot_data(edinburgh_run)  # Calling the plot function

