#
# python_grabber
#

from pygrabber.dshow_graph import *


class PyGrabber:
    def __init__(self, callback):
        self.graph = FilterGraph()
        self.callback = callback

    def get_devices(self):
        return self.graph.get_input_devices()

    def get_formats(self):
        return self.graph.get_formats()

    def set_device(self, input_device_index):
        self.graph.add_input_device(input_device_index)

    def display_format_dialog(self):
        self.graph.display_format_dialog()

    def start(self, handle):
        self.graph.add_sample_grabber(self.callback)
        self.graph.add_default_render()
        self.graph.prepare()
        self.graph.configure_render(handle)
        self.graph.run()

    def stop(self):
        self.graph.stop()

    def update_window(self, width, height):
        self.graph.update_window(width, height)

    def set_device_properties(self):
        self.graph.set_properties(self.graph.get_input_device())

    def grab_frame(self):
        self.graph.grab_frame()
