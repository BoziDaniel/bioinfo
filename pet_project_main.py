import pet_project_data_manager as dm
import pet_project_ui as ui
import sys
import os


def clear():
    os.system('clear')


def choose():
    inputs = ui.user_input("\nSelect an option: ")
    if inputs == "1":
        DNA_sequence = ui.user_input("\nAdd DNA: ")
        protein = dm.DNA_to_protein(DNA_sequence)
        print(f"\nSTOP in protein: {dm.count_STOP_in_protein(protein)}")
        print(f"protein: {protein}\n")
        dm.option_to_save_file(protein)
    elif inputs == "2":
        RNA_sequence = ui.user_input("\nAdd RNA: ")
        protein = dm.RNA_to_protein(RNA_sequence)
        print(f"protein: {protein}\n")
        dm.option_to_save_file(protein)
    elif inputs == "3":
        DNA_sequence = ui.user_input("\nAdd DNA: ")
        RNA_complementer = dm.DNA_to_RNA(DNA_sequence)
        print(f"RNA: {RNA_complementer}\n")
        dm.option_to_save_file(RNA_complementer)
    elif inputs == "4":
        RNA_sequence = ui.user_input("\nAdd RNA: ")
        DNA = dm.RNA_to_DNA(RNA_sequence)
        print(f"DNA: {DNA}\n")
        dm.option_to_save_file(DNA)
    elif inputs == "5":
        DNA_sequence = ui.user_input("\nAdd DNA: ")
        complementer = dm.DNA_complementer_creation(DNA_sequence)
        print(f"DNA complementer: {complementer}\n")
        dm.option_to_save_file(complementer)
    elif inputs == "6":
        file_name = ui.user_input("\nAdd existing file name: ")
        dm.open_existing_file(file_name)
    elif inputs == "0":
        sys.exit()
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = [" DNA -> protein ",
               " RNA -> protein ",
               " DNA -> RNA ",
               " RNA -> DNA ",
               " DNA complementer creation ",
               " Open existing file "]

    ui.print_menu("Main menu:", options, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == "__main__":
    main()
