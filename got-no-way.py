import os


def get_path() -> str:
    return input('Please enter path -> ')


def get_file_list(path_to_file: str) -> list:
    directory = None
    try:
        directory = os.listdir(path_to_file)
    except:
        show_error('Error opening file.')
    return directory


def show_error(text_to_display: str):
    print(text_to_display)


def show_results(results: list):
    print(results)


def get_files_starting_with_name(file_list: list, name: str) -> list:
    result_list = [check_name(file, name) for file in file_list if check_name(file, name) is not None]

    return result_list


def check_name(file: str, name: str) -> str:
    return file if file[:len(name)] == name else None


if __name__ == '__main__':
    path = get_path()

    files = get_file_list(path)

    results = get_files_starting_with_name(files, 'deep')

    show_results(results)
