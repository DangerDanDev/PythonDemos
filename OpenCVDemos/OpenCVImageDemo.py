import cv2
import tkinter
import numpy
import PIL.Image
import PIL.ImageTk


class Image:
    '''
    A wrapper class for OpenCV's image class system.
    It loads an image using cv2.imread(filepath), pulls the height, width, and channel numbers from it,
    and then stores a reference to it as a tkinter.PhotoImage (self.photo_image) which can be passed onto
    a canvas object.
    '''
    height: int
    width: int
    channels: int

    data: numpy.ndarray # potatoes

    # The image in a format that tkinter can process
    photo_image: tkinter.PhotoImage

    def __init__(self, filepath: str):
        self.load_image(filepath)

    def load_image(self, filepath: str):
        """
        Loads an image from a filepath and returns the image as a numpy.ndarray object\n
        :param filepath: The location of the image file
        :return: image as numpy.ndarray
        """
        # Load the image from CV2
        self.data = cv2.imread(filepath)

        # Get the height, width, and channels of the image.
        # This function requires numpy!
        self.height, self.width, self.channels = self.data.shape

        self.photo_image = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(self.data))


# Create my tkinter window
window = tkinter.Tk()
window.title('OpenCV Image Demo')

img = Image('../../Python/PythonDemos2/background.png')

# Create a canvas large enough to hold the image, put the image on it, and anchor it to the northern corner of
# The canvas. Then pack it into the window.
canvas = tkinter.Canvas(window, width=img.width, height=img.height)
canvas.create_image(0, 0, image=img.photo_image, anchor=tkinter.NW)
canvas.pack()

# Finally we get to run the window loop
window.mainloop()

