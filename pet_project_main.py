import pet_project_data_manager as dm
import pet_project_ui as ui
import sys
import os


def clear():
    os.system('clear')


def choose():
    inputs = ui.user_input("\nSelect an option: ", ["0", "1", "2", "3", "4", "5", "6"])
    if inputs == "1":
        DNA_sequence = ui.user_input("\nAdd DNA: ", ["A", "T", "C", "G"])
        protein = dm.DNA_to_protein(DNA_sequence)
        print(f"protein: {protein}\n")
        print(f"STOP in protein: {dm.count_STOP_in_protein(protein)}")
        dm.option_to_save_file(protein)
        clear()
    elif inputs == "2":
        RNA_sequence = ui.user_input("\nAdd RNA: ", ["A", "U", "C", "G"])
        protein = dm.RNA_to_protein(RNA_sequence)
        print(f"protein: {protein}\n")
        print(f"STOP in protein: {dm.count_STOP_in_protein(protein)}")
        dm.option_to_save_file(protein)
        clear()
    elif inputs == "3":
        DNA_sequence = ui.user_input("\nAdd DNA: ", ["A", "T", "C", "G"])
        RNA_complementer = dm.DNA_to_RNA(DNA_sequence)
        print(f"RNA: {RNA_complementer}\n")
        dm.option_to_save_file(RNA_complementer)
        clear()
    elif inputs == "4":
        RNA_sequence = ui.user_input("\nAdd RNA: ", ["A", "U", "C", "G"])
        DNA = dm.RNA_to_DNA(RNA_sequence)
        print(f"DNA: {DNA}\n")
        dm.option_to_save_file(DNA)
        clear()
    elif inputs == "5":
        DNA_sequence = ui.user_input("\nAdd DNA: ", ["A", "T", "C", "G"])
        complementer = dm.DNA_complementer_creation(DNA_sequence)
        print(f"DNA complementer: {complementer}\n")
        dm.option_to_save_file(complementer)
        clear()
    elif inputs == "6":
        file_name = input("\nAdd existing file name: ")
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
    clear()
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == "__main__":
    main()
