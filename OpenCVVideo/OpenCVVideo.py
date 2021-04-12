import tkinter
import cv2


class MyVideoCapture:
    """

    """
    vid: cv2.VideoCapture

    def __init__(self, video_source=0):
        '''

        :param video_source:
        '''
        self.vid = cv2.VideoCapture(video_source)

        if not self.vid.isOpened():
            raise ValueError('Unable to open video source: ', video_source)

        # Get the video width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_XI_HEIGHT)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


class App:
    """

    """
    # The main window for the app
    window: tkinter.Tk = tkinter.Tk()

    def __init__(self, window_title, video_src: cv2.VideoCapture = 0):
        self.window.title(window_title)

        self.video_source = video_src

        # Open the video capture source
        self.vid = MyVideoCapture(video_src)

        self.canvas = tkinter.Canvas(self.window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        self.window.mainloop()


App('Name')