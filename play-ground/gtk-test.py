# This code use gtk which is window tool-kit not
# default with mac.
# To use GTK with python, for mac, install the following:
# brew install gtk4
# brew install pygobject3
# and use python3.12. It may not work with python3.9
# Note that brew may install pygobject not regular dir of python. Thus, it is required to set PYTHONPATH appropriately. It is possibly under /opt/homebrew.

# Also, for different version, different pip module would be appropriate. Therefore, to use PyOpenGL, do the following
# python3.12 -m venv $HOME/py312
# source $HOME/py312/bin/activate
# The above makes python ver 3.12 as default.
# Then, run the following for opengl for python 3.12.
# pip install pyopengl

# The following is partially cited from Qiita. Sorry, I forgot a URL.

# GTK related code, esp, GLArea is come from the following URL: https://athenajc.gitbooks.io/python-gtk-3-api/content/

# Note that some modern OpenGL code is come from
# https://gist.github.com/TurBoss/78dd883ba045d311695d7b30eab8a5be
# for sample purpose.

# gtk3
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Gdk", "4.0")
from gi.repository import Gtk
from gi.repository import Gdk

from OpenGL.GL import *
from OpenGL.GLU import *

from OpenGL.arrays import vbo
from OpenGL.GL import shaders
from OpenGL.raw.GL.ARB.vertex_array_object import glGenVertexArrays, glBindVertexArray

from numpy import array
import numpy as np

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        # self.area = Gtk.GLArea()
        self.glView = MyGLView()
        # self.add(self.glView)
        # self.glView = Gtk.GLArea()

        self.stack = Gtk.Stack()
        self.set_child(self.stack)
        self.stack.add_named(self.glView, "GL")

        self.set_size_request(400, 400)
        print(self.stack.get_visible_child())
        button = Gtk.Button.new_with_label("Test")

        # self.glView.show()
        # self.stack.add_named(button, "Button")
        print(self.stack.get_visible_child())

class MyGLView(Gtk.GLArea):
    def __init__(self):
        super().__init__()

        print("GL ver set")
        self.set_required_version(3, 3)

        # self.test_features()

        self.set_size_request(400, 400)
        self.set_vexpand(True)
        self.set_hexpand(True)
        self.set_visible(True)

        # self.connect('renderp', self.on_render)
        self.connect('render', self.on_render_new)
        self.connect('realize', self.on_realize)
        # self.connect('resize', self.on_resize)

        # print(self.get_preferred_height())
        # print(self.get_preferred_width())

    def on_resize(self, area, width, height, user_data):
        print("resize")
        glClear(GL_COLOR_BUFFER_BIT)

        # draw your object  
        glColor3f(0, 0, 1)           
        glBegin(GL_TRIANGLES)
        glVertex3f ( 0.0, 1.0, 0.0)
        glVertex3f (-1.0,-1.0, 0.0)
        glVertex3f ( 1.0,-1.0, 0.0)
        glEnd()
        glFlush()

        # we completed our drawing; the draw commands will be
        # flushed at the end of the signal emission chain, and
        # the buffers will be drawn on the window
        return True

    def on_render(self, area, context):
        # area.make_current()
        context.make_current()

        # debug
        print("legacy")
        print(Gdk.GLContext.is_legacy(context))
        print("on_render")
        # end of debug

        # debug
        # glDeleteTextures (1, 0)
        # glBindTexture(GL_TEXTURE_2D, 0)
        # glDeleteTextures (1, 1)
        # glBindTexture(GL_TEXTURE_2D, 1)
        # enf of debug

        # inside this function it's safe to use GL; the given
        # Gdk.GLContext has been made current to the drawable
        # surface used by the Gtk.GLArea and the viewport has
        # already been set to be the size of the allocation
        # we can start by clearing the buffer        
        glClearColor(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT)

        # draw your object  
        # glColor3f(0.0, 0.0, 1.0)           
        glBegin(GL_TRIANGLES)
        glVertex3f ( 0.0, 1.0, 0.0)
        glVertex3f (-1.0,-1.0, 0.0)
        glVertex3f ( 1.0,-1.0, 0.0)
        glEnd()
        glFlush()

        # we completed our drawing; the draw commands will be
        # flushed at the end of the signal emission chain, and
        # the buffers will be drawn on the window
        return True

    # Modern OpenGL ver of render signal.
    def on_render_new(self, widget, context):
        context.make_current()
        widget.attach_buffers()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glUseProgram(self.shader)

        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        glBindVertexArray(0)

        # glUseProgram(0)
        glFlush()

    def on_realize(self, area):        
        # We need to make the context current if we want to
        # call GL API
        # area.make_current()   
        context = area.get_context()
        # context.require_version(3, 3)
        # context.set_profile(Gtk.GLArea.Profile.CORE)
        context.make_current()
        # self.attach_buffers()

        # debug
        print("on_realize")
        # end of debug        

        self.initOpenGL(area)

        print("after init OpenGL")

        # If there were errors during the initialization or
        # when trying to make the context current, this
        # function will return a Gio.Error for you to catch
        if (area.get_error() != None):
          return      

        w = area.get_allocated_width()
        h = area.get_allocated_height()
        glViewport(0, 0, w, h)

        glClearColor(1.0, 0.0, 0.0, 0.0)
        # glClear(GL_COLOR_BUFFER_BIT)

        print(self.get_auto_render())

        self.set_auto_render(True)

        # self.init_buffers()
        # self.init_shaders()

    def initOpenGL(self, area):
        # For modern OpenGL
        _vertices = [
            0.6, 0.6, 0.0, 1.0,
            -0.6, 0.6, 0.0, 1.0,
            0.0, -0.6, 0.0, 1.0]

        self.vertices = np.array(_vertices, dtype=np.float32)

        # self.vertex_array_object = glGenVertexArrays(1, self.vertex_array_object)
        # glBindVertexArray(self.vertex_array_object)

        self.vao = GLuint(0)
        glGenVertexArrays(1, self.vao)
        glBindVertexArray(self.vao)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, len(self.vertices) * sizeof(GLfloat), self.vertices, GL_STATIC_DRAW)


        # glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, stride=0, offset=0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0)
        glEnableVertexAttribArray(0)

        return self
    
    def test_features(self):
        print('Testing features')
        print('glGenVertexArrays Available %s' % bool(glGenVertexArrays))
        print('Alpha Available %s' % bool(self.get_has_alpha()))
        print('Depth buffer Available %s' % bool(self.get_has_depth_buffer()))

def on_app_activate(app):
    return True

VERTEX_SHADER = """
    #version 330
    in vec4 position;
    void main()
    {
        gl_Position = position;
    }"""

FRAGMENT_SHADER = """
    #version 330
    out vec4 fragColor;
    void main()
    {
        fragColor = vec4(1.0, 0.0, 0.0, 1.0);
    }
    """

# win = Gtk.Window()
# glViewport(0, 0, 100, 100)
win = MyWindow()
# win = Gtk.ComboBox()
# win = Gtk.Button()

# The following does not work. This is because it is supposed that event propagation problem for render problem would be there.
# win = MyGLView()

# win.connect("destroy", Gtk.main_quit)
win.show()
win.present()
# win.show()
# Gtk.main()

app = Gtk.Application()
app.connect('activate', on_app_activate)
app.run()
