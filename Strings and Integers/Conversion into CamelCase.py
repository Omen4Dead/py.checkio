import re


def to_camel_case(name: str) -> str:
    # replace this for solution
    copy_name = name
    name = name.capitalize()
    for i in re.findall('_[a-z]', copy_name):
        name = name.replace(str(i), str(i).upper().strip('_'))
    return name


print("Example:")
print(to_camel_case("my_function_name"))

# These "asserts" are used for self-checking
assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
