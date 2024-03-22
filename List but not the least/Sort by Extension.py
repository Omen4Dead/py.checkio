import re


def sort_by_ext(files: list[str]) -> list[str]:
    # your code here
    pattern = r'\b\.[a-z0-9]+$'
    split_files = []
    for file in files:
        extension = re.findall(pattern, file)
        extension = extension[0] if len(extension) > 0 else ''
        name = file.removesuffix(extension)
        split_files.append((extension, name))
    split_files = sorted(split_files)
    new_files_list = []
    for ext, name in split_files:
        new_files_list.append(name + ext)
    return new_files_list


print("Example:")
print(sort_by_ext(["1.cad", "1.bat", "1.aa", 'str1.str2.str3', '.config', '.str1.str2', 'config']))

# These "asserts" are used for self-checking
assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
    "1.aa",
    "1.bat",
    "2.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
    ".bat",
    "1.aa",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
    ".aa",
    ".bat",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    "1.aa.doc",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    ".aa.doc",
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
