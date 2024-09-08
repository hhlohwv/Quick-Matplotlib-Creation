"""
Template code for generating publication quality plots
"""

# Module Import
import os

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker  # for tick location formatting
import addcopyfighandler  #not called explicitly, adds ctrl+c feature to plots


#%% Plot data import
x = [0,1,2,3,4,5]
y = [0,1,2,3,4,5]


#%% Main Plotting Function
# Global plot formatting
mpl.rcParams['savefig.format'] = 'svg' # sets copied file to .svg
mpl.rcParams['savefig.bbox'] = 'tight' # reduces white space around fig
mpl.rcParams['pdf.fonttype'] = 42  # compatibility with adobe illustrator
mpl.rcParams['ps.fonttype'] = 42 # also recommended from website
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['text.color'] = 'black'
mpl.rcParams['legend.edgecolor'] = 'black'  # color of legend text
mpl.rcParams['legend.fancybox'] = 'False'  # rounded edges of legend frame
mpl.rcParams['legend.frameon'] = 'True'
mpl.rcParams['lines.linewidth'] = 2.5  # linewidth of plots
mpl.rcParams['legend.facecolor'] = 'white'  # legend background color
mpl.rcParams['legend.framealpha'] = 1  # transparency of legend background



# Plot 1
fig = plt.figure(figsize=(8,6)) # create canvas
# define axes, lower left corner pos, length of axes (on 0-1 scale)
ax = plt.axes((0.1,0.1,0.7,0.8))  

# Defining line plots and axis limits
ax.plot(x,y, label='test')
ax.set_xlim((0,3)) # set x axis limit
ax.set_ylim((0,10))  # set y axis limit

# Formatting of plot elements
ax2.yaxis.set_major_formatter('{x:.0f}')  # label formatting 
# loc sets which corner of legend is used to anchor, bbox sets position
ax.legend(loc='upper right', bbox_to_anchor=(1.3,1), frameon=False, \
          fontsize=12)
ax.tick_params(axis='both', labelsize=12)
font_xaxis = {'family':'Arial', 'color':'black', 'weight':'normal', \
             'size':13}
ax.set_xlabel('Frequency (THz)', fontdict=font_xaxis)
font_yaxis = {'family':'Arial', 'color':'black', 'weight':'normal', \
             'size':14}
ax.set_ylabel('n', labelpad=12, rotation=0, fontdict=font_yaxis)
font_title = {'size':13}
ax.set_title(f'Refractive Index with nominal thickness (330$\mu$m)',\
             fontdict=font_title, pad=7.0)

fig.show()
