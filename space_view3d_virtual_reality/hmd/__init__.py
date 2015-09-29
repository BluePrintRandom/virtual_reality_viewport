
TODO = True

from mathutils import (
        Matrix,
        Vector,
        )

import gpu


# ############################################################
# Data structs
# ############################################################

def HMD(display_backend):
    """
    return the head mounted display device class
    (defined in another file)

    :param display_backend: asdasd
    :type display_backend: str
    """
    from .oculus import Oculus
    from .debug import Debug

    displays = {
            'OCULUS':Oculus,
            'DEBUG':Debug,
            }

    if display_backend not in displays:
        assert False, "Display Backend \"{0}\" not implemented".format(display_backend)

    return displays[display_backend]()


# ############################################################
# Data structs
# ############################################################

class HMD_Data:
    status = None
    projection_matrix = Matrix()
    modelview_matrix = Matrix()
    interpupillary_distance = Vector((0.0, 0.0))
    width = 0
    height = 0
    fbo_id = 0
    texture_id = 0


# ############################################################
# Base class inherited by HMD devices
# ############################################################

class HMD_Base:
    __slots__ = {
        "_fbo",
        "_height",
        "_interpupillary_distance",
        "_modelview_matrix",
        "_name",
        "_offscreen_object",
        "_projection_matrix",
        "_texture",
        "_width",
        }

    def __init__(self, name):
        self._name = name
        self._projection_matrix = Matrix.Identity(4)
        self._modelview_matrix = Matrix.Identity(4)
        self._interpupillary_distance = Vector((0.0, 0.0))
        self._width = 0
        self._height = 0
        self._fbo_id = 0
        self._texture_id = 0
        self._offscreen_object = None

    @property
    def offscreen_object(self):
        return self._offscreen_object

    @property
    def fbo(self):
        return self._fbo_id

    @property
    def texture(self):
        return self._texture_id

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def projection_matrix(self):
        return self._projection_matrix

    @property
    def modelview_matrix(self):
        TODO # calculate
        return self._modelview_matrix

    def isConnected(self):
        """
        Check if device is connected

        :return: return True if the device is connected
        :rtype: bool
        """
        assert False, "isConnected() not implemented for the \"{0}\" device".format(self._name)

    def init(self):
        """
        Initialize device

        :return: return True if the device was properly initialized
        :rtype: bool
        """
        try:
            self._offscreen_object = gpu.offscreen_object_create(self._width, self._height)
            self._fbo_id = self._offscreen_object.framebuffer_object
            self._texture_id = self._offscreen_object.color_object

        except Exception as E:
            print(E)
            return False

        else:
            return True

    def loop(self):
        """
        Get fresh tracking data
        """
        assert False, "loop() not implemented for the \"{0}\" device".format(self._name)

    def frameReady(self):
        """
        The frame is ready to be send to the device
        """
        assert False, "frameReady() not implemented for the \"{0}\" device".format(self._name)

    def quit(self):
        """
        Garbage collection
        """
        try:
            gpu.offscreen_object_free(self._offscreen_object)

        except Exception as E:
            print(E)

