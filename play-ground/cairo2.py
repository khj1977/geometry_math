# test code from https://palepoli.skr.jp/tips/pygobject/drawingarea.php#google_vignette

import sys, gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import cairo as c
 
class Win(Gtk.ApplicationWindow):
    '''
        draw のサンプル
    '''
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app, title='Py')
        area = Gtk.DrawingArea()
        # How to obtain context is not match with on_draw() for ignal of area of Gtk.DrawingArea.
        self.cont = c.Context
        area.connect('draw', self.on_draw)
        self.add(area)
        self.resize(300, 100)
        self.show_all()
 
    def on_draw(self, widget, cr):
    # def on_draw(self, cr):
        # サイズ取得
        # cr = self.cont        
        # cr = cr.Context
        aw = widget.get_allocated_width()
        ah = widget.get_allocated_height()
        # 黒で全体を塗りつぶす、RGB を 0.0 から 1.0 の範囲で指定
        # cr.set_source_rgb(0.1, 0.1, 0.1)
        # cr.rectangle(0, 0, aw, ah)
        # cr.fill()
        # グレーで線を引く
        cr.set_source_rgb(0.5, 0.5, 0.5)
        cr.set_line_width(5.0)
        cr.move_to(aw, 0)
        cr.line_to(0, ah)
        cr.stroke()
        # 白で文字列描写、基準位置は左下、改行未対応
        cr.set_source_rgb(1, 1, 1)
        cr.select_font_face('Monospace', 0, 0)
        cr.set_font_size(48)
        cr.move_to(5, ah - 5)
        cr.show_text('AIAIAIAIAI')
        # 等幅になっているのを確認
 
class App(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)
 
    def do_startup(self):
        Gtk.Application.do_startup(self)
        Win(self)
 
    def do_activate(self):
        self.props.active_window.present()
 
app = App()
app.run(sys.argv)