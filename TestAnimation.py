import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(0, 1024))
line, = ax.plot([], [], lw=1)

#MAX_POINTS = 10
MAX_POINTS = 100
#MAX_POINTS = 1000

#MAX_DELAY_BETWEEN_FRAMES_MS = 1
#MAX_DELAY_BETWEEN_FRAMES_MS = 10
MAX_DELAY_BETWEEN_FRAMES_MS = 50
#MAX_DELAY_BETWEEN_FRAMES_MS = 100
#MAX_DELAY_BETWEEN_FRAMES_MS = 1000

x_axis_arr = list()
y_axis_arr = list()

for i in range(0, MAX_POINTS):
  x_axis_arr.append(i)
  y_axis_arr.append(i)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    #returns an array evenly spaced
    x_axis_arr = np.linspace(0, 2, MAX_POINTS)
    
    y_axis_arr.pop()#Pop the end
    getVar = 100 + random.uniform(0,500) 
    #getVar = i * 5
    #print(str(type(getVar)) + " " + str(getVar))
    
    y_axis_arr.insert(0, getVar)#Insert at start
    line.set_data(x_axis_arr, y_axis_arr)

    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=MAX_POINTS, interval=MAX_DELAY_BETWEEN_FRAMES_MS, blit=True)




# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])





plt.show()
