# "Dev tools" is the base menu that gives you easy access to the individual tools I've wrote to help me with GUI and game development.
# Any tool script file you add to your game will add a button to this menu.
# Dev tools menu is accessible by pressing ~ button (under Esc). you can drag the menu around the screen.
# Remove the tools before publishing your game.

# Requirements: None

init -100:
    # icon , Action
    define dev_tools = [
        ["✖", Hide('dev_tools_s')],
    ]

init python:
    config.underlay.append(
        renpy.Keymap(
            K_BACKQUOTE=lambda: renpy.run(ToggleScreen("dev_tools_s"))
        )
    )

screen dev_tools_s:
    style_prefix "dev_tools"
    zorder 1100
    use dev_tools_keys
    drag:
        align(1.0, 0.0) offset(-100, 100)
        frame:
            xmaximum 1000
            hbox:
                box_wrap True
                for i in dev_tools:
                    button:
                        text i[0]
                        action i[1]

style devtools_text:
    font "DejaVuSans.ttf"
