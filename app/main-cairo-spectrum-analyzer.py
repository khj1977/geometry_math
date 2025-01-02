# To use this app, cairo on OS and pycairo for python is required to be installed.
# It may be:
# brew install cairo (if it were mac)
# pip install pycairo
# Check actual install command by yourself.

# Every time open source stack to make program?
# Actually, I checked specification of
# CoreGraphics of mac and Objective-C and that 
# seems impressive. However, it would be 
# derivative of PostScript. Commercial code
# or middle ware is better than open source?
# For ultimate case, we need to mentenance 
# code of middle ware or even required to hack it.
# Moreover it seems cairo is derivative of 
# PostScript and share some base with 
# CoreGraphics. 
# 
# Python or Objective-C? Objective-C is compile 
# lang, inherit good things from Smalltalk as well
# as Foundation, AppKit and other libs as Cocoa or
# other framework. However, python is compact and 
# elegant and clean as it behave as pseudo 
# code In addtion to good manner as programming 
# lang, libs with python is still good for 
# practical use, esp, scipy/numpy.
# Moreover, python is open source. Python seems
# better than Objective-C for my case. Thus, 
# I determined to use python and cairo.

import cairo
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib

from math import pi
import math as m

from com_gmail_eulerbonjour.digital_signal import fft_and_audio_cairo as mic

# audioMod = mic.MicAndFFT()

def drawFFT(ctx):
    global audioMod

    audioMod.readDataAndDoFFT(ctx)

# Mainly but not all, the GTK part of following code is come from https://gist.github.com/ritobanrc/cf61e574ffb89eae2b3837d8dc2328c6 for test purpose.

width = 512
height = 256

def on_draw_time(da: Gtk.DrawingArea, ctx: cairo.Context):
    data = audioMod.getTimeSeriesData()

    ctx.set_line_width(1.0)
    ctx.move_to(10.0, 20.0)

    x = 0.0
    xx = 0.0
    yy = 0.0
    stepX = 0.3
    multipleY = -30.0
    centreY = 100
    for y in data:
        
        xx = x + 10.0
        yy = (height - 20.0 * y * multipleY) * 1.0 - centreY
        ctx.line_to(xx, yy)
        ctx.move_to(xx, yy)

        x = x + stepX

    ctx.stroke()

def on_draw_fft(da: Gtk.DrawingArea, ctx: cairo.Context):
    """
    A callback called every time `drawingarea.queue_draw` is called.
    """
    alloc = da.get_allocation()
    width = alloc.width
    height = alloc.height

    audioMod.readDataAndDoFFT(ctx)

    # draw(ctx, width, height)

def on_mouse_pressed(da, event, *data):
    """
    This is called when the mouse is pressed
    """
    print("The mouse was pressed!")

def main():
    """
    The main function
    """

    global audioMod

    # Create a window, set it up to quit on close
    win = Gtk.Window()
    win.connect('destroy', Gtk.main_quit)
    win.set_default_size(width, height*2)

    box = Gtk.VBox()
    win.add(box)

    # Create a DrawingArea, add it to the window, and connect it to the `on_draw` function

    drawingareaTime = Gtk.DrawingArea()
    box.add(drawingareaTime)
    drawingareaTime.connect('draw', on_draw_time)

    drawingarea = Gtk.DrawingArea()
    box.add(drawingarea)
    drawingarea.connect('draw', on_draw_fft)

    # Add a button pressed event, and connect it to the `on_mouse_pressed` callback
    drawingarea.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
    drawingarea.connect('button-press-event', on_mouse_pressed)

    # Tell the drawing area to render
    drawingarea.queue_draw()
    drawingareaTime.queue_draw()

    def refresh_screen():
        drawingarea.queue_draw()
        drawingareaTime.queue_draw()
        GLib.timeout_add(1000 / 60, refresh_screen)

    # Normally, GUI Libraries don't automatically redraw the screen every
    # frame. In order to do that, I've setup a timer to call `refresh_screen`
    # in 16.666 milliseconds (60 FPS). `refresh_screen`, queues a draw command
    # to re-draw the drawing area and then re-adds the timer for the next
    # frame. This might seem like a hack, but its more-or-less the "correct"
    # way to implement this.
    # 
    # If this is not the behavior you want (perhaps you only want your fractal
    # to re-draw when the mouse button is pressed), remove this line and the
    # `refresh_screen` function, and call `drawingarea.queue_draw()`.from
    # somewhere else 
    GLib.timeout_add(1000 / 60, refresh_screen)

    # Show the window
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    audioMod = mic.MicAndFFT(height, width)
    main()