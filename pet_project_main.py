import pet_project_data_manager
import pet_project_ui
import sys
import os


def clear():
    os.system('clear')


def choose():
    inputs = pet_project_ui.user_input("\nSelect an option: ")
    if inputs == "1":
        DNA_sequence = pet_project_ui.user_input("\nAdd DNA: ")
        protein = pet_project_data_manager.DNA_to_protein(DNA_sequence)
        print(f"STOP in protein: {pet_project_data_manager.count_STOP_in_protein(protein)}")
        print(f"protein: {protein}\n")
        pet_project_data_manager.option_to_save_file(protein)
    elif inputs == "2":
        RNA_sequence = pet_project_ui.user_input("\nAdd RNA: ")
        protein = pet_project_data_manager.RNA_to_protein(RNA_sequence)
        print(f"protein: {protein}\n")
        pet_project_data_manager.option_to_save_file(protein)
    elif inputs == "3":
        DNA_sequence = pet_project_ui.user_input("\nAdd DNA: ")
        RNA_complementer = pet_project_data_manager.DNA_to_RNA(DNA_sequence)
        print(f"RNA: {RNA_complementer}\n")
        pet_project_data_manager.option_to_save_file(RNA_complementer)
    elif inputs == "4":
        RNA_sequence = pet_project_ui.user_input("\nAdd RNA: ")
        DNA = pet_project_data_manager.RNA_to_DNA(RNA_sequence)
        print(f"DNA: {DNA}\n")
        pet_project_data_manager.option_to_save_file(DNA)
    elif inputs == "5":
        DNA_sequence = pet_project_ui.user_input("\nAdd DNA: ")
        complementer = pet_project_data_manager.DNA_complementer_creation(DNA_sequence)
        print(f"DNA complementer: {complementer}\n")
        pet_project_data_manager.option_to_save_file(complementer)
    elif inputs == "6":
        pass
        # file_name = pet_project_data_manager.user_input("\nAdd existing file name: ")
        #open file(file_name) and show
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


<<<<<<< HEAD
=======
def option_to_save_file(result):
    y_or_n = pet_project_data_manager.user_input("\nWould you like to save the file? y/n ")
    if y_or_n == "y":
        file_name = pet_project_data_manager.user_input("\nAdd a file name following with .txt: ")
        pet_project_data_manager.handle_file(file_name, result)


>>>>>>> 72a3372463277546910418bc5df9eff9d35c2e6e
def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            pet_project_ui.print_error_message(str(err))


if __name__ == "__main__":
    main()
