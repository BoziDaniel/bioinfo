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
    """else:
        print("wrong input")
        sys.exit()
"""


def main():
    print_main()
    choose()
    

if __name__ == "__main__":
    main()