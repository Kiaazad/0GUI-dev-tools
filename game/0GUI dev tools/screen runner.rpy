# Add these two lines to add your screen into runner lst
# init python:
#     try:
#         scr_run_lst.append(["Name", action])
#     except:
#         pass

# Requirements: None

init -96 python:
    try:
      dev_tools.append(["ᐉ", ToggleScreen('scr_run',list= scr_run_lst)])
    except:
        pass
init -100:
    define scr_run_lst = []

init -100:
    define scr_run_lst = []
screen scr_run(list):
    zorder 1090
    drag:
        frame:
            vbox:
                for i in list:
                    button:
                        text i[0]
                        action i[1]