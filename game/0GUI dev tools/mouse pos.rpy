# It shows the window size, mouse position and have two button to get pos(x, x) and align(0.x, 0.x)
# You can change the accuracy of align in the configuration part by hitting the gear

# Requirements: clip.rpy

init -99 python:
    try:
       dev_tools.append(["ტ", ToggleScreen('mouse_inf')])
    except:
        pass
    
init python:
    def get_pos_alg(strip = 3):
        w, h = config.screen_width, config.screen_height
        x, y = renpy.get_mouse_pos()
        if x and y:
            ax = str(float(x)/w)[:strip+2]
            ay = str(float(y)/h)[:strip+2]
            alg = 'align({}, {})'.format(ax, ay)
        else:
            alg = "mouse possibly Out of screen"
        return 'pos({}, {})'.format(x, y) ,  alg

screen mouse_inf():
    style_prefix "devtools"
    zorder 1100
    default conf = 0
    default strip = 3
    timer .1 repeat True action SetScreenVariable("conf",conf)
    drag:
        yalign .1
        frame:
            vbox:
                text 'current window size is {}'.format( renpy.get_physical_size() )
                text get_pos_alg(strip)[0]
                text get_pos_alg(strip)[1]

                hbox:
                    button:
                        text "✖"
                        action Hide('mouse_inf')
                    button:
                        text "⚙"
                        action ToggleScreenVariable('conf',true_value=1, false_value=0)
                    button:
                        text "get pos"
                        action Show("mouseinf_get_pos")
                    button:
                        text "get align"
                        action Show("mouseinf_get_alg", strip = strip)

                if conf:
                    vbox:
                        hbox:
                            text "align's floating points: "
                            textbutton "< " action If(strip > 1,SetScreenVariable("strip",strip-1))
                            text str(strip)
                            textbutton " >" action SetScreenVariable("strip",strip+1)

screen mouseinf_get_pos:
    button:
        background "#00f5"
        action [Function(clip_put, get_pos_alg()[0]),Hide("mouseinf_get_pos")]

screen mouseinf_get_alg(strip):
    button:
        background "#0f05"
        action [Function(clip_put, get_pos_alg(strip)[1]),Hide("mouseinf_get_alg")]
