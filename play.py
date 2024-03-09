import pygame
import pygame_menu as pm

pygame.init()

# Экран
WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Стандартные цвета RGB
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Основная функция программы
def main():
    ms = pm.Menu(title="плеер",
                 width=WIDTH,
                 height=HEIGHT,
                 theme=pm.themes.THEME_GREEN)

    play = pm.Menu(title="игры",
                   width=WIDTH,
                   height=HEIGHT,
                   theme=pm.themes.THEME_GREEN)

    # Настройка значений по умолчанию
    play.get_theme().widget_font_size = 25
    play.get_theme().widget_font_color = BLACK
    play.get_theme().widget_alignment = pm.locals.ALIGN_LEFT

    play.add.button(title="плеер", action=ms, font_color=WHITE, background_color=GREEN, align=pm.locals.ALIGN_CENTER)

    # Создание меню настроек
    settings = pm.Menu(title="настройки",
                       width=WIDTH,
                       height=HEIGHT,
                       theme=pm.themes.THEME_GREEN)

    # Настройка значений по умолчанию
    settings.get_theme().widget_font_size = 25
    settings.get_theme().widget_font_color = BLACK
    settings.get_theme().widget_alignment = pm.locals.ALIGN_LEFT

    # Переключатели для включения/выключения музыки и звука
    settings.add.toggle_switch(
        title="Muisc", default=True, toggleswitch_id="music")
    settings.add.toggle_switch(
        title="Sounds", default=False, toggleswitch_id="sound")

    # Часы, отображающие текущую дату и время
    settings.add.clock(clock_format="%d-%m-%y %H:%M:%S",
                       title_format="время : {0}")

    # 3 разные кнопки, каждая со своим стилем и назначением
    settings.add.button(title="сбросить настройки", action=settings.reset_value,
                        font_color=WHITE, background_color=RED)
    settings.add.button(title="вернутся на главное меню",
                        action=pm.events.BACK, align=pm.locals.ALIGN_CENTER)

    # Создание главного меню
    main_menu = pm.Menu(title="главное меню",
                        width=WIDTH,
                        height=HEIGHT,
                        theme=pm.themes.THEME_GREEN)

    main_menu.add.button(title="игры", action=play, font_color=WHITE, background_color=GREEN,
                         align=pm.locals.ALIGN_CENTER)

    # Кнопка, которая ведет в меню настроек при нажатии
    main_menu.add.button(title="настройки", action=settings,
                         font_color=WHITE, background_color=GREEN, align=pm.locals.ALIGN_LEFT)

    # Пустая метка, которая используется для разделения двух кнопок
    main_menu.add.label(title="")

    # Кнопка выхода, которая используется для завершения программы
    main_menu.add.button(title="выйти", action=pm.events.EXIT,
                         font_color=WHITE, background_color=RED, align=pm.locals.ALIGN_CENTER)

    # Позволяет отображать главное меню на экране
    main_menu.mainloop(screen)


if __name__ == "__main__":
    main()
