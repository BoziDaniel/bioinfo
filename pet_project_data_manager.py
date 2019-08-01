import pet_project_ui as ui
import pet_project_AA_code_dictionary as AA_code_table


def DNA_complementer_creation(DNA_template):
    complementer = ""
    for base in DNA_template:
        if base == "A":
            complementer += "T"
        elif base == "T":
            complementer += "A"
        elif base == "C":
            complementer += "G"
        elif base == "G":
            complementer += "C"
        else:
            ui.print_error_message("contains an invalid base")
            break
    return complementer


def DNA_to_RNA(DNA_template):
    DNA_complementer = DNA_complementer_creation(DNA_template)
    RNA_complementer = ""
    for base in DNA_complementer:
        if base == "A":
            RNA_complementer += "U"
        elif base == "T":
            RNA_complementer += "A"
        elif base == "C":
            RNA_complementer += "G"
        elif base == "G":
            RNA_complementer += "C"
        else:
            ui.print_error_message("contains an invalid base")
            break
    return RNA_complementer


def RNA_to_DNA(RNA):
    DNA_complementer_to_RNA = ""
    for base in RNA:
        if base == "A":
            DNA_complementer_to_RNA += "T"
        elif base == "U":
            DNA_complementer_to_RNA += "A"
        elif base == "C":
            DNA_complementer_to_RNA += "G"
        elif base == "G":
            DNA_complementer_to_RNA += "C"
        else:
            ui.print_error_message("contains an invalid base")

    RNA_complementer = DNA_complementer_creation(DNA_complementer_to_RNA)
    return RNA_complementer


def RNA_to_protein(RNA):
    triplet_lenght = 3
    RNA_pcs = [RNA[i:i+triplet_lenght] for i in range(0, len(RNA), triplet_lenght)]
    protein = []
    for triplet in RNA_pcs:
        if len(triplet) < 3:
            pass
        else:
            protein.append(AA_code_table.AA_dict.get(triplet))
    protein = "-".join(protein)
    return protein


def DNA_to_protein(DNA):
    RNA_complementer = DNA_to_RNA(DNA)
    protein = RNA_to_protein(RNA_complementer)
    return protein


def count_STOP_in_protein(protein):
    number_of_STOPS = protein.count("STOP")
    return number_of_STOPS


def option_to_save_file(result):
    y_or_n = ui.user_input("\nWould you like to save the file? y/n ", ["y", "n"])
    if y_or_n == "y":
        file_name = input("\nAdd a file name following with .txt: ")
        handle_file(file_name, result)


def handle_file(file_name, result):
    file = open(file_name, "x")
    file = open(file_name, "a")
    file.write(result)
    file.close()


def open_existing_file(file_name):
    while True:
        try:
            with open(file_name, "r") as file:
                text = file.read()
        except FileNotFoundError as error:
            print(error)
            break
        else:
            print("\n" + text + "\n")
            break
