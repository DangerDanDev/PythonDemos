import tkinter

import PIL.ImageTk
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
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        print('Width: ', self.width)
        print('Height: ', self.height)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()

            # Return a boolean success flag and the current frame converted to BGR
            if ret:
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return ret, None


class App:
    """

    """
    # The main window for the app
    window: tkinter.Tk = tkinter.Tk()

    def __init__(self, window_title, video_src: cv2.VideoCapture = 0):

        # The delay in frame udpates on the video-canvas
        self.delay = 5

        self.window.title(window_title)

        self.video_source = video_src

        # Open the video capture source
        self.vid = MyVideoCapture(video_src)

        self.canvas = tkinter.Canvas(self.window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        self.update()
        self.window.mainloop()


    def update(self):

        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        # If we have a returned frame:
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor = tkinter.NW)

        # Calls the update method in the graphics thread after the
        # Given delay time
        self.window.after(self.delay, self.update)


App('Name', 0)#, r"C:\Users\dange\Downloads\video.mp4")
