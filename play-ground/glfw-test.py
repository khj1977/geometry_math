# A sample of glfw is come from the following.
# https://qiita.com/Dhichisutto/items/76ec93c690caf20cedb9

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from gi.repository import GLib as G

import glfw
from OpenGL.GL import *

def on_activate(app):
    return None

def on_idle(user_data):
    # glfw.wait_events()
    return None

def button_clicked(button, user_data):
    print("clicked")

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.stack = Gtk.Stack()
        self.set_child(self.stack)

        self.set_size_request(400, 400)
        # print(self.stack.get_visible_child())
        self.button = Gtk.Button.new_with_label("Test")
        
        self.button.connect("clicked", button_clicked)

        self.stack.add_named(self.button, "Button")
        # print(self.stack.get_visible_child())

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINE_LOOP)
    glVertex2d(-0.9, -0.9)
    glVertex2d( 0.9, -0.9)
    glVertex2d( 0.9,  0.9)
    glVertex2d(-0.9,  0.9)
    glEnd()

    glfw.swap_buffers(window)

def init():
    glClearColor(0.0, 0.0, 1.0, 1.0)
    display()   # necessary only on Windows

def window_refresh(window):
    display()

if not glfw.init():
    raise RuntimeError('Could not initialize GLFW3')

window = glfw.create_window(300, 300, 'prog1 5.1', None, None)
if not window:
    glfw.terminate()
    raise RuntimeError('Could not create an window')

glfw.set_window_refresh_callback(window, window_refresh)
glfw.make_context_current(window)

init()

# GTK
win = MyWindow()

# win.connect("destroy", Gtk.main_quit)
win.show()
win.present()

app = Gtk.Application()
app.connect('activate', on_activate)
# GLib.idle_add(on_idle, None)
# app.run()

mainContext = G.MainContext()
while not glfw.window_should_close(window):
    # g_main_context_iteration (NULL, TRUE);
    # It may be better to put the following glib method to be under idle func of glfw if there exists.
    # G.MainContext.iteration(None, True)
    
    # it is dangerous to comment out wait_events() and enable i = 1 with idle_func for wait event.
    glfw.wait_events()
    mainContext.iteration(False)

glfw.terminate()