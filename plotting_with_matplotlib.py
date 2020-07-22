import matplotlib.pyplot as plt
import numpy as np

# simple bar and scatter plot
x = np.arange(5) # assume there are 5 students
y = (20, 35, 30, 35, 27) # their test scores
plt.bar(x,y) # Barplot
# need to close the figure using show() or close(), if not closed any

plt.show() # Try commenting this an run
plt.scatter(x,y) # scatter plot
plt.show()

########################################################################################
# More plotting details                                                                  
########################################################################################

# generate sample data
x = np.linspace(0, 20, 1000) #100 evenly-spaced values from 0 to 50
y = np.sin(x)
# customize axis labels
plt.plot(x, y, label = 'Sample Label')
plt.title('Sample Plot Title') # chart title
plt.xlabel('x axis label') # x axis title
plt.ylabel('y axis label') # y axis title
plt.grid(True) # show gridlines
# add footnote
plt.figtext(0.995, 0.01, 'Footnote', ha='right', va='bottom')
# add legend, location pick the best automatically
plt.legend(loc='best', framealpha=0.5, prop={'size':'small'})
# tight_layout() can take keyword arguments of pad, w_pad and h_pad.
# these control the extra padding around the figure border and between subplots.
# The pads are specified in fraction of fontsize.
plt.tight_layout(pad=1)
# Saving chart to a file
plt.savefig('filename.png')
#plt.close() # Close the current window to allow new plot creation on
            #separate window / axis, alternatively we can use show()
plt.show()

########################################################################################
# The Figure is the top-level
# container for everything on a canvas. Axes is a container class for a specific plot. A Figure
# may contain many axes and/or subplots. Subplots are laid out in a grid within the Figure.
# Axes can be placed anywhere on the Figure. We can use the subplots factory to get the
# Figure and all the desired axes at once
########################################################################################

fig, ax = plt.subplots()
fig,(ax1,ax2,ax3,ax4) = plt.subplots(nrows=4, ncols=1, sharex=True, figsize=(8,4))
# Iterating the Axes within a Figure
for ax in fig.get_axes():
    pass # do something

########################################################################################
# ax_plot() example                                                                 
########################################################################################

# generate sample data
x = np.linspace(0, 20, 1000)
y = np.sin(x)

fig = plt.figure(figsize=(8,4)) # get an empty figure and add an Axes
ax = fig.add_subplot(1,1,1) # row-col-num

ax.plot(x, y, 'b-', linewidth=2, label='Sample label') # line plot data on the Axes

# add title, labels and legend, etc.
ax.set_ylabel('y axis label', fontsize=16) # y label
ax.set_xlabel('x axis label', fontsize=16) # x label
ax.legend(loc='best') # legend
ax.grid(True) # show grid
fig.suptitle('Sample Plot Title') # title
fig.tight_layout(pad=1) # tidy laytout
fig.savefig('filename.png', dpi=125)

