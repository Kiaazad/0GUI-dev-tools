# a simple function that puts a string into the clipboard
init python:
    import pygame.scrap
    def clip_put(m):
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, m.encode("utf-8"))
