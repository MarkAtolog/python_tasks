import itertools
import os


def get_latest_file_with_extension(dir_path: str, file_extension: str):
    files = [(file, os.stat(os.path.join(dir_path, file)).st_ctime)
             for file in os.listdir(dir_path)
             if file.endswith(file_extension)]
    files.sort(key=lambda file: file[1], reverse=True)
    latest_files = [file[0] for file in
                    list(itertools.takewhile(lambda file: file[1] > files[0][1] - 10, files))]
    return latest_files[0], latest_files[1:]


def get_difference_with_collections(list1: list, list2: list) -> list:
    return list(set(list1) - set(list2))


def get_difference_without_collections(list1: list, list2: list) -> list:
    return [x for x in list1 if x not in list2]


def file_manipulation(path_to_txt_file: str, line_numbers=(10,)):
    with open(path_to_txt_file, "r+") as input_file:
        lines = input_file.readlines()
        cut_lines = []
        for n in line_numbers:
            cut_lines.append(lines.pop(n))
        with open(f"{path_to_txt_file.strip('.txt')}_res.txt", "w") as new_file:
            new_file.writelines(cut_lines)
        input_file.seek(0)
        input_file.truncate()
        input_file.writelines(lines)


if __name__ == '__main__':
    path = ""
    extension = ""
    print(get_latest_file_with_extension(path, extension))

    list1 = ["Alex", "Dima", "Kate", "Galina", "Ivan"]
    list2 = ["Dima", "Ivan", "Kate"]
    print(get_difference_with_collections(list1, list2))
    print(get_difference_without_collections(list1, list2))

    file_manipulation("file.txt")
