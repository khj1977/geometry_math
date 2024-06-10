# This code use gtk which is window tool-kit not
# default with mac.
# To use GTK with python, for mac, install the following:
# brew install gtk+3
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

# gtk3
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from OpenGL.GL import *
from OpenGL.GLU import *

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        # self.area = Gtk.GLArea()
        self.glView = MyGLView()
        # self.add(self.glView)
        # self.glView = Gtk.GLArea()

        self.stack = Gtk.Stack()
        self.add(self.stack)
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

        self.set_size_request(400, 400)
        self.set_vexpand(True)
        self.set_hexpand(True)
        self.set_visible(True)

        # self.connect('renderp', self.on_render)
        self.connect('render', self.on_render)
        self.connect('realize', self.on_realize)
        self.connect('resize', self.on_resize)

        print(self.get_preferred_height())
        print(self.get_preferred_width())

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
        area.make_current()

        # debug
        print("render")
        # end of debug

        # inside this function it's safe to use GL; the given
        # Gdk.GLContext has been made current to the drawable
        # surface used by the Gtk.GLArea and the viewport has
        # already been set to be the size of the allocation
        # we can start by clearing the buffer        
        # glClearColor(0, 0, 0, 0)
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

    def on_realize(self, area):        
        # We need to make the context current if we want to
        # call GL API
        area.make_current()    

        # debug
        print("realize")
        # end of debug        

        # If there were errors during the initialization or
        # when trying to make the context current, this
        # function will return a Gio.Error for you to catch
        if (area.get_error() != None):
          return      

        w = area.get_allocated_width()
        h = area.get_allocated_height()
        glViewport(0, 0, w, h)

        glClearColor(1.0, 0, 0, 0)
        # glClear(GL_COLOR_BUFFER_BIT)

        print(self.get_auto_render())

        self.set_auto_render(True)

        # self.init_buffers()
        # self.init_shaders()

# win = Gtk.Window()
# glViewport(0, 0, 100, 100)
win = MyWindow()
# win = Gtk.ComboBox()
# win = Gtk.Button()

# The following does not work. This is because it is supposed that event propagation problem for render problem would be there.
# win = MyGLView()

win.connect("destroy", Gtk.main_quit)

win.show_all()
# win.show()
Gtk.main()