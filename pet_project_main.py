import pet_project_data_manager
import pet_project_ui
import sys


def choose():
    inputs = pet_project_ui.user_input("\nSelect an option: ")
    if inputs == "1":
        DNA_sequence = pet_project_ui.user_input("\nAdd DNA: ")
        protein = pet_project_data_manager.DNA_to_protein(DNA_sequence)
        print(f"protein: {protein}\n")        
    elif inputs == "2":
        RNA_sequence = pet_project_ui.user_input("\nAdd RNA: ")
        protein = pet_project_data_manager.RNA_to_protein(RNA_sequence)
        print(f"protein: {protein}\n")
    elif inputs == "3":
        DNA_sequence = pet_project_ui.user_input("\nAdd DNA: ")
        RNA_complementer = pet_project_data_manager.DNA_to_RNA(DNA_sequence)
        print(f"RNA: {RNA_complementer}\n")
    elif inputs == "4":
        RNA_sequence = pet_project_ui.user_input("\nAdd RNA: ")
        DNA = pet_project_data_manager.RNA_to_DNA(RNA_sequence)
        print(f"DNA: {DNA}\n")
    elif inputs == "5":
        pass
    elif inputs == "6":
        DNA_sequence = pet_project_ui.user_input("\nAdd DNA: ")
        complementer = pet_project_data_manager.DNA_complementer_creation(DNA_sequence)
        print(f"DNA complementer: {complementer}\n")
    elif inputs == "0":
        sys.exit()
    else:
        raise KeyError("There is no such option.")
 

def handle_menu():
    options = [" DNA -> protein ",
               " RNA -> protein ",
               " DNA -> RNA ",
               " RNA -> DNA ",
               " Compare 2 DNA ",
               " DNA complementer creation "]

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