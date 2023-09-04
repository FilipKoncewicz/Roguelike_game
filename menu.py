from picture import PICTURE_MENU,PICTURE_MENU_2,PICTURE_STORY_1,PICTURE_STORY_2,PICTURE_STORY_3,INPUT_PICTURE
from util import clear_screen
from sys import exit
from main import initiate_game
from music import menu_music,head_music,story_music


def display_menu():
    """
    Menu display function.

    Args:
         Lack

    Returns:
         option (str): variable that stores the user's choice
    """
    print(PICTURE_MENU)
    print(PICTURE_MENU_2)
    option = input(INPUT_PICTURE)
    return option


def get_menu_option():
    """
    A function that retrieves a menu selection from the user i
    confirming compliance with the requirements.

    Args:
        Lack

    Returns:
        option (str): variable that stores the user's choice
    """
    option = display_menu()
    choices = ['1', '2',]

    while True:
        if option in choices:
            return option
        else:
            clear_screen()
            print("Invalid option. Try again.")
            option = display_menu()


def run_game():
    """
    The function retrieves the menu option from the user and runs further functions depending on the selection.

    Args:
        Lack

    Returns:
        Lack
    """
    PLAY = '1'
    EXIT = '2'
    menu_music()
    game_mode = get_menu_option()

    if game_mode == PLAY:
        clear_screen()
        story_music()
        display_story()
        head_music()
        initiate_game()
    elif game_mode == EXIT:
        exit()


def display_story():
    print(PICTURE_STORY_1)
    input('''              
........
 ''')
    print(PICTURE_STORY_2)
    input('''              
........
 ''')
    print(PICTURE_STORY_3)
    input('''              
........
 ''')
    clear_screen()