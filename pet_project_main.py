import pet_project_data_manager
import pet_project_ui
import sys


def choose():
    inputs = pet_project_ui.user_input
    if inputs == "1":
        pass
    elif inputs == "2":
        pass
    elif inputs == "3":
        pass
    elif inputs == "4":
        pass
    elif inputs == "5":
        pass
    elif inputs == "0":
        sys.exit()
    else:
        raise KeyError("There is no such option.")
        

def handle_menu():
    options = [" DNS -> protein ",
               " RNS -> protein ",
               " DNS -> RNS ",
               " RNS -> DNS ",
               " Compare 2 DNS "]

    pet_project_ui.print_menu("Main menu:", options, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            pet_project_ui.print_error_message(str(err))
    

if __name__ == "__main__":
    main()