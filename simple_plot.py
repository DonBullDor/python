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
