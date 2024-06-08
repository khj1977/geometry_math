# This code use gtk which is window tool-kit not
# default with mac.
# For mac, install the following:
# brew install gtk+3
# brew install pygobject3
# and use python3.12. It may not work with python3.9

# gtk3
import gi

gi.require_version("Gtk", "3.0") # 👈
from gi.repository import Gtk

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit) # 👈
win.show_all() # 👈
Gtk.main() # 👈