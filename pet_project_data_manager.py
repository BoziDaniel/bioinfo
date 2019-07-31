import pet_project_ui
import pet_project_AA_code_dictionary
import re


def DNA_complementer_creation(inputs):
    complementer = ""
    for base in inputs:
        if base == "A":
            complementer += "T"
        elif base == "T":
            complementer += "A"
        elif base == "C":
            complementer += "G"
        elif base == "G":
            complementer += "C"
        else:
            pet_project_ui.print_error_message("contains an invalid base")
            break
    return complementer


def DNA_to_RNA(inputs):
    DNA_complementer = DNA_complementer_creation(inputs)
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
            pet_project_ui.print_error_message("contains an invalid base")
            break
    return RNA_complementer


def RNA_to_DNA(inputs):
    RNA = inputs
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
            pet_project_ui.print_error_message("contains an invalid base")
            break
    RNA_complementer = DNA_complementer_creation(DNA_complementer_to_RNA)
    return RNA_complementer


def RNA_to_protein(inputs):
    n = 3
    RNA_pcs = [inputs[i:i+n] for i in range(0, len(inputs), n)]
    protein = []
    for triplet in RNA_pcs:
        if len(triplet) < 3:
            pass
        else:
            protein.append(pet_project_AA_code_dictionary.AA_dict.get(triplet))
    protein = "-".join(protein)
    return protein


def DNA_to_protein(inputs):
    RNA_complementer = DNA_to_RNA(inputs)
    protein = RNA_to_protein(RNA_complementer)
    result = (protein)
    return result
    return protein


def count_STOP_in_protein(protein):
    STOPs_in_protein = []
    STOPs_in_protein.append(re.search("STOP.", protein))
    return len(STOPs_in_protein)


def option_to_save_file(result):
    y_or_n = pet_project_ui.user_input("\nWould you like to save the file? y/n ")
    if y_or_n == "y":
        file_name = pet_project_ui.user_input("\nAdd a file name following with .txt: ")
        handle_file(file_name, result)


def handle_file(inputs, result):
    file = open(inputs, "x")
    file = open(inputs, "a")
    file.write(result) 
    file.close()


