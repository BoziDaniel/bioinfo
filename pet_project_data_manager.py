import pet_project_ui
import pet_project_AA_code_dictionary


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
    RNA_complementer = ""
    for base in inputs:
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


def RNA_to_protein(inputs):
    n = 3
    RNA_pcs = [inputs[i:i+n] for i in range(0, len(inputs), n)]
    protein = []
    for triplet in RNA_pcs:
        protein.append(pet_project_AA_code_dictionary.AA_dict.get(triplet))

    protein = "".join(protein)
    
    return protein

