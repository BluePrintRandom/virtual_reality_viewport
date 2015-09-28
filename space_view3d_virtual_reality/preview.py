"""
Viewport Preview Drawing
************************

Routines to draw in the viewport the result
that is projected in the HMD
"""

from .opengl_helper import (
        draw_rectangle,
        view_reset,
        view_setup,
        )

from bgl import *

TODO = True


class Preview:
    __slots__ = {
            "_texture",
            "_width",
            "_height",
            }

    def init(self, texture, width, height):
        """
        Initialize preview window

        :param texture: 2D Texture binding ID (bind to the Framebuffer Object)
        :type texture: bgl.GLint
        :param width: Horizontal dimension of preview window
        :type width: int
        :param height: Vertical dimension of preview window
        :type height: int
        """
        self._texture = texture
        self.update(texture, width, height)

    def quit(self):
        """
        Destroy preview window
        """
        pass

    def update(self, texture, width, height):
        """
        Resize preview window

        :param texture: 2D Texture binding ID (bind to the Framebuffer Object)
        :type texture: bgl.GLint
        :param width: Horizontal dimension of preview window
        :type width: int
        :param height: Vertical dimension of preview window
        :type height: int
        """
        self._texture = texture
        self._width = width
        self._height = height

    def loop(self, scale):
        """
        Draw in the preview window
        """
        if not scale:
            return

        texture = self._texture

        act_tex = Buffer(GL_INT, 1)
        glGetIntegerv(GL_ACTIVE_TEXTURE, act_tex)

        if scale != 100:
            viewport = Buffer(GL_INT, 4)
            glGetIntegerv(GL_VIEWPORT, viewport)

            width = int(scale * 0.01 * viewport[2])
            height = int(scale * 0.01 * viewport[3])

            glViewport(viewport[0], viewport[1], width, height)
            glScissor(viewport[0], viewport[1], width, height)

            glEnable(GL_DEPTH_TEST)
            glDepthFunc(GL_LESS)

        view_setup()

        glEnable(GL_TEXTURE_2D)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, texture)

        draw_rectangle()

        glBindTexture(GL_TEXTURE_2D, act_tex[0])

        glDisable(GL_TEXTURE_2D)
        glDisable(GL_DEPTH_TEST)

        view_reset()

        if scale != 100:
            glViewport(viewport[0], viewport[1], viewport[2], viewport[3])
            glScissor(viewport[0], viewport[1], viewport[2], viewport[3])

