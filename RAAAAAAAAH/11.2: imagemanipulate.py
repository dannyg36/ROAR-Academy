from matplotlib import image
from matplotlib import pyplot
import os

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
data = image.imread(filename)

path2 = os.path.dirname(os.path.abspath(__file__))
filename2 = path + '/' + 'smallchinaflag.bmp'
data2 = image.imread(filename2)

# Display image information
print('Image type is: ', type(data))
print('Image shape is: ', data.shape)

# Add some color boundaries to modify an image array
flag_data = data2.copy()
plot_data = data.copy()
for width in range(262,512):
    for height in range(250):
        plot_data[height][width] = flag_data[height][width-262]

# Write the modified images
image.imsave(path+'/'+'lenna-mod.jpg', plot_data)

# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()