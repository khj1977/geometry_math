# This test/sample code is come from query to Gemini.

import cairo

# サーフェスを作成
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 100, 100)

# コンテキストを作成
ctx = cairo.Context(surface)

# 線の太さを設定
ctx.set_line_width(2.0)

# 描画
ctx.move_to(10, 10)
ctx.line_to(90, 90)
ctx.stroke()

# 画像として保存
surface.write_to_png('line.png')