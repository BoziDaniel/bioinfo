import pet_project_ui


def DNA_comlementer_creation(inputs):
    complementer = ""
    for base in inputs:
        if base == A:
            complementer += T
        elif base == T:
            base += A
        elif base == C:
            base += G
        elif base += G:
            base += C
        else:
            pet_project_ui.print_error_message("contains an invalid base")
            break

