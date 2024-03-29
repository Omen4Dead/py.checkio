import re


def from_camel_case(name: str) -> str:
    # replace this for solution
    copy_name = name
    for i in re.findall('[A-Z]', copy_name):
        name = name.replace(str(i), '_' + str(i).lower())
    name = name.strip('_')
    return name


print("Example:")
print(from_camel_case("MyFunctionName"))

# These "asserts" are used for self-checking
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
