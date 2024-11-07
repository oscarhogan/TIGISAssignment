TIGIS Python Practical Assignment
=================================

This repository includes two python files, one corresponding to each of the two tasks. 

'tone' includes a function associated with Task 1. It reads the included 'plenty.data' file and converts them into floats. They are placed within a pair of lists with x giving all x values and y giving the set of y values corresponding with each x. The data points are then plotted using the matplotlib library


'ttwo' includes a function associated with Task 2. It reads the 'natural_neighbourhoods' file and reproduces the data in the form of a dictionary holding the name of each neighbourhood as a key along with a list of tuples containing coordinate x,y values. The data is then plotted in the form of polygons to a map extent using matplotlib and cartopy.

Installation Instructions 
-------------------------
Download data and python files from within this repository, storing  within your working directory.

Usage 
-----
Open both python files within a code editor of your choice, with python enabled, run 'tone' to obtain the first plotted outcome then run 'ttwo' to receive the final map outcome.

Map Design Rationale
--------------------
As the outputs function is to provide a means to locate each neighbourhood within Edinburgh I identified clarity, valuing a minimalist design philosophy as a priority. The inclusion
of components such as axis labelling and grid lines seeks only to detract from the aesthetic value of the map outcome itself with the consistent blue theme providing a coherent smooth visual. 