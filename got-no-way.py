import os


def get_path() -> str:
    return input('Please enter path -> ')


def get_file_list(path_to_directory: str) -> list:
    '''
    :param path_to_driectory: path to directory as string
    :return: a list that contains the names of all files inside directory
    '''
    return os.listdir(path_to_directory)


def show_results(results: list):
    print(results)


def get_files_starting_with_name(file_list: list, name: str) -> list:
    return [check_name(file, name) for file in file_list if check_name(file, name) is not None]


def check_name(file_name: str, name_to_search: str) -> str:
    return file_name if file_name[:len(name_to_search)] == name_to_search else None


if __name__ == '__main__':
    path = get_path()
    files = get_file_list(path)
    results = get_files_starting_with_name(files, 'deep')
    show_results(results)
