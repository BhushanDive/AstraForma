import pygame, sys
import pygame_gui
pygame.init()

WINDOW_SIZE = (800, 600)
isRunning = True

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

background = pygame.Surface(WINDOW_SIZE)
background.fill(pygame.Color(0, 255, 255))

manager = pygame_gui.UIManager(WINDOW_SIZE)

hello_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((350, 275), (100, 50)),
                                                                      text = 'Play',
                                                                      manager = manager)

clock = pygame.time.Clock()

while isRunning:
    clock.tick(60)
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Lets Play')
        manager.process_events(event)
    manager.update(time_delta)

    screen.blit(background, (0, 0))
    manager.draw_ui(screen)
    pygame.display.update()
