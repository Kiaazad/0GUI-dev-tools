# Requirements: clip.rpy

init -97 python:
    try:
       dev_tools.append(["✐", ToggleScreen('color_pick')])
    except:
        pass

init python:
    def color_calc(r, g, b, a):
        if a == 255:
            h1 = '#{:02x}{:02x}{:02x}'.format(r, g , b)
            h2 = '#'+'{:02x}'.format(r)[0]+'{:02x}'.format(g)[0]+'{:02x}'.format(b)[0]
            rgb = '{}, {}, {}'.format(r, g , b)
        else:
            h1 = '#{:02x}{:02x}{:02x}{:02x}'.format(r, g , b, a)
            h2 = '#'+'{:02x}'.format(r)[0]+'{:02x}'.format(g)[0]+'{:02x}'.format(b)[0]+'{:02x}'.format(a)[0]
            rgb = '{}, {}, {}, {}'.format(r, g , b, a)
        return h1, h2, rgb
default persistent.color_pick_scheme = []
screen color_pick:
    default r = 255
    default g = 200
    default b = 0
    default a = 200

    default conf = 0

    drag:
        frame:
            background None
            hbox:
                vbox:
                    spacing 5
                    hbox:
                        spacing 100
                        hbox:
                            spacing -100 ysize 300
                            frame:
                                yalign 0.0 xysize(200, 200) background color_calc(r, g, b, a)[0]
                                text color_calc(r, g, b, a)[0] yalign 0.0
                            frame:
                                yalign 1.0 xysize(200, 200) background color_calc(r, g, b, a)[1]
                                text color_calc(r, g, b, a)[1] yalign 1.0
                
                        frame:
                            align(1.0, 1.0) padding(10,10)
                            vbox:
                                button:
                                    xysize(40,40) background None
                                    text "⊞" size 40
                                    action AddToSet(persistent.color_pick_scheme, color_calc(r, g, b, a))
                                button:
                                    xysize(40,40) background None
                                    text "⊡" size 40
                                    action ToggleScreen("color_pick_swatch")
                                button:
                                    xysize(40,40) background None
                                    text "⚙" size 40
                                    action ToggleScreenVariable("conf",1,0)
                                button:
                                    xysize(40,40) background None
                                    text "✖" size 40
                                    action Hide('color_pick')
                    bar value ScreenVariableValue("r",255) range 255 xsize 512 ysize 20 left_bar Solid((r, 0, 0, 255)) right_bar Solid((255, 0, 0, 100)) thumb None
                    bar value ScreenVariableValue("g",255) range 255 xsize 512 ysize 20 left_bar Solid((0, g, 0, 255)) right_bar Solid((0, 255, 0, 100)) thumb None
                    bar value ScreenVariableValue("b",255) range 255 xsize 512 ysize 20 left_bar Solid((0, 0, b, 255)) right_bar Solid((0, 0, 255, 100)) thumb None
                    bar value ScreenVariableValue("a",255) range 255 xsize 512 ysize 20 left_bar Solid((r, g, b, a)) right_bar Solid((0, 0, 0, 100)) thumb None


screen color_pick_swatch:
    style_prefix "devtools"
    default siz = 40
    default dis = 10
    default conf = 0
    drag:
        xalign 0.9
        frame:
            xsize 512 background None padding(0,0)
            vbox:
                hbox:
                    frame:
                        xfill True
                        hbox:
                            xalign 0.0
                            button:
                                xysize(40,40) background None
                                text "✖" size 40
                                action Hide('color_pick_swatch')
                            button:
                                xysize(40,40) background None
                                text "⚙" size 40
                                action ToggleScreenVariable("conf",1,0)
                if conf:
                    vbox:
                        bar value ScreenVariableValue("siz",200) range 200 ysize 20
                        bar value ScreenVariableValue("dis",100) range 100 ysize 20
                hbox:
                    box_wrap True
                    spacing dis box_wrap_spacing dis
                    for i in persistent.color_pick_scheme:
                        button:
                            xysize(siz,siz)
                            background i[0]
                            action Show("color_pick_scheme_opt",i=i )

screen color_pick_scheme_opt(i):
    drag:
        frame:
            background i[0]
            vbox:
                hbox:
                    xsize 280
                    button:
                        xysize(40,40) background None xalign 0.0
                        text "⊟" size 40
                        action RemoveFromSet(persistent.color_pick_scheme, i), Hide("color_pick_scheme_opt")
                    text "copy"
                    button:
                        xysize(40,40) background None xalign 1.0
                        text "✖" size 40
                        action Hide('color_pick_scheme_opt')
                button:
                    text i[1]
                    action Function(clip_put, '"'+i[1]+'"'), Hide("color_pick_scheme_opt")
                button:
                    text i[0]
                    action Function(clip_put, '"'+i[0]+'"'), Hide("color_pick_scheme_opt")
                button:
                    text i[2]
                    action Function(clip_put, i[2]), Hide("color_pick_scheme_opt")
