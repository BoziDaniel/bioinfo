import pet_project_data_manager
import pet_project_ui
import sys
import os


def clear():
    os.system('clear')


def choose():
    inputs = pet_project_ui.user_input("\nSelect an option: ", ["A", "U", "C", "G"])
    if inputs == "1":
        DNA_sequence = pet_project_ui.user_input("\nAdd DNA: ", ["A", "U", "C", "G"])
        protein = pet_project_data_manager.DNA_to_protein(DNA_sequence)
        print(f"STOP in protein: {pet_project_data_manager.count_STOP_in_protein(protein)}")
        print(f"protein: {protein}\n")
        pet_project_data_manager.option_to_save_file(protein)
    elif inputs == "2":
        RNA_sequence = pet_project_ui.user_input("\nAdd RNA: ", ["A", "U", "C", "G"])
        protein = pet_project_data_manager.RNA_to_protein(RNA_sequence)
        print(f"protein: {protein}\n")
        pet_project_data_manager.option_to_save_file(protein)
    elif inputs == "3":
        DNA_sequence = pet_project_ui.user_input("\nAdd DNA: ", ["A", "U", "C", "G"])
        RNA_complementer = pet_project_data_manager.DNA_to_RNA(DNA_sequence)
        print(f"RNA: {RNA_complementer}\n")
        pet_project_data_manager.option_to_save_file(RNA_complementer)
    elif inputs == "4":
        RNA_sequence = pet_project_ui.user_input("\nAdd RNA: ", ["A", "U", "C", "G"])
        DNA = pet_project_data_manager.RNA_to_DNA(RNA_sequence)
        print(f"DNA: {DNA}\n")
        pet_project_data_manager.option_to_save_file(DNA)
    elif inputs == "5":
        DNA_sequence = pet_project_ui.user_input("\nAdd DNA: ", ["A", "U", "C", "G"])
        complementer = pet_project_data_manager.DNA_complementer_creation(DNA_sequence)
        print(f"DNA complementer: {complementer}\n")
        pet_project_data_manager.option_to_save_file(complementer)
    elif inputs == "6":
        file_name = pet_project_ui.user_input("\nAdd existing file name: ", ["A", "U", "C", "G"])
        pet_project_data_manager.open_existing_file(file_name)
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
