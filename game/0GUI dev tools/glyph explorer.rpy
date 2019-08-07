# Requirements: clip.rpy

init -97 python:
    try:
      dev_tools.append(["₯", ToggleScreen('glyphEx')])
    except:
        pass

init python:
    class glyph_ex():
        def __init__(self):
            self.lst = []
            self.ind = 0
            self.page = 1
            self.per = 200
            self.fill()
        def fill(self):
            self.lst = []
            while len(self.lst) < self.per:
                if not self.ind == 91 and not self.ind == 123:
                    self.lst.append(self.ind)
                self.ind += 1
        def next(self, s = 0):
            if self.ind < 65335:
                if self.ind + self.per*s < 65335:
                    self.ind += self.per*s
                self.fill()
        def back(self, s = 0):
            self.ind -= self.per*(2+s)
            if self.ind < self.per:
                self.ind = 0
            self.fill()
default glyph_ex_ins = glyph_ex()

        
        
init offset = -1

screen glyphEx(f = glyph_ex_ins):
    default copied = ""
    modal True
    style_prefix "glyphx"
    add "#000a"
    key "q" action Function(f.back)
    key "e" action Function(f.next)

    button:
        align(1.0,0.0) offset(-20,20)
        text "✖"
        action Hide("glyphEx")

    hbox:
        align(0.0,0.0) offset(20,20)
        frame:
            ysize 74 xminimum 74
            text copied
        button:
            xsize None
            text "Copy"
            action Function(clip_put, copied)
        button:
            xsize None
            text "Clear"
            action SetScreenVariable("copied", "")


    hbox:
        align(.5,0.0) offset(0,20)
        button:
            text "⇇"
            action Function(f.back, 4)
        button:
            text "←"
            action Function(f.back)
        frame:
            ysize 74 xsize 200
            text str(f.ind) 
        button:
            text "→"
            action Function(f.next)
        button:
            text "⇉"
            action Function(f.next, 4)
    hbox:
        xsize 1680 box_wrap True box_wrap_spacing 10 yoffset 50
        for i in f.lst:
            if i <= 65335:
                button:
                    text unichr(i) style "glyphxS_btns"
                    action SetScreenVariable("copied", copied+unichr(i))


style glyphxS_btns:
    size 40
    # font "0GUI dev tools/fonts/HAMMBL__.TTF"

style glyphx_button:
    xysize(74,74)
    hover_sound None