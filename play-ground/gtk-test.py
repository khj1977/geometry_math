# This code use gtk which is window tool-kit not
# default with mac.
# To use GTK with python, for mac, install the following:
# brew install gtk+3
# brew install pygobject3
# and use python3.12. It may not work with python3.9

# The following is cited from Qiita. Sorry, forgot URL.

# GTK related code, esp, GLArea is come from the following URL: https://athenajc.gitbooks.io/python-gtk-3-api/content/

# gtk3
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        # self.area = Gtk.GLArea()
        self.area = MyGLView()
                          
        self.add(self.area)

class MyGLView(Gtk.GLArea):
    def __init__(self):
        super().__init__()
        self.connect('render', self.on_render)
        self.connect('realize', self.on_realize)

    def on_render(self, area, context):
        area.make_current()

        # debug
        print("render")
        # end of debug

        w = area.get_allocated_width()
        h = area.get_allocated_height()
        glViewport(0, 0, w, h)

        # inside this function it's safe to use GL; the given
        # Gdk.GLContext has been made current to the drawable
        # surface used by the Gtk.GLArea and the viewport has
        # already been set to be the size of the allocation
        # we can start by clearing the buffer        
        glClearColor(0, 0, 0, 0)
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

        # self.init_buffers()
        # self.init_shaders()

# win = Gtk.Window()
win = MyWindow()
win.connect("destroy", Gtk.main_quit)

win.show_all()
Gtk.main()