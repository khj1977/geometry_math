import cairo
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib

from math import pi
import math as m

from com_gmail_eulerbonjour.digital_signal import fft_and_audio_cairo as mic

audioMod = mic.MicAndFFT()

def drawFFT(ctx):
    global audioMod

    audioMod.readDataAndDoFFT(ctx)

# Mainly but not all, the GTK part of following code is come from https://gist.github.com/ritobanrc/cf61e574ffb89eae2b3837d8dc2328c6 for test purpose.

width = 256
height = 256

angle = 45

def draw(ctx: cairo.Context, width, height):
    """
    This is the draw function, that will be called every time `queue_draw` is
    called on the drawing area. Currently, this is setup to be every frame, 60
    times per second, but you can change that by changing line 95. 
    
    Ported from the first example here, with minimal changes:
    https://www.cairographics.org/samples/
    """

    global angle
    angle += 1

    xc = 128
    yc = 128
    radius = 100
    angle1 = angle  * (pi/180)
    angle2 = 180 * (pi/180)

    ctx.set_line_width(10.0 * m.sin(angle * 0.01))
    ctx.arc(xc, yc, radius, angle1, angle2)
    ctx.stroke()

    # draw helping lines
    ctx.set_source_rgba (1, 0.2, 0.2, 0.6)
    ctx.set_line_width (6.0)

    ctx.arc(xc, yc, 10.0, 0, 2*pi)
    ctx.fill()

    ctx.arc(xc, yc, radius, angle1, angle1)
    ctx.line_to(xc, yc)
    
    # Adding this fixes a subtle bug where when the two hands would overlap. 
    # This just makes them two separate strokes. 
    ctx.stroke() 
    ctx.arc(xc, yc, radius, angle2, angle2)
    ctx.line_to(xc, yc)
    ctx.stroke()


def on_draw(da: Gtk.DrawingArea, ctx: cairo.Context):
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
    win.set_default_size(width, height)

    # Create a DrawingArea, add it to the window, and connect it to the `on_draw` function
    drawingarea = Gtk.DrawingArea()
    win.add(drawingarea)
    drawingarea.connect('draw', on_draw)


    # Add a button pressed event, and connect it to the `on_mouse_pressed` callback
    drawingarea.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
    drawingarea.connect('button-press-event', on_mouse_pressed)

    # Tell the drawing area to render
    drawingarea.queue_draw()

    def refresh_screen():
        drawingarea.queue_draw()
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
    audioMod = mic.MicAndFFT()
    main()