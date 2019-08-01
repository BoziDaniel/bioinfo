def print_error_message(message):
    print(f'Error: {message}')


def print_menu(title, list_options, exit_message):
    count = 1
    print("\t" + title)
    for element in list_options:
        print(f"\t({count}) {element}")
        count += 1
    print(f"\t({0})  {exit_message}")


def user_input(question, valid_characters):
    while True:
        try:
            inputs = input(f"{question}")
            for i in inputs:
                if i not in valid_characters:
                    raise (ValueError, TypeError)
            break
        except (ValueError, TypeError):
            print("Iiiiii")
    return inputs

