# Cracking the Coding Interview
# Problem 1.6
# simple string compression: aabbbcc -> a2b3c2
# if "compressed" string does not save space, return original string
# only Upper and Lower letters a-z


def compress_str(string):
    compressed_string = ""
    counter = 1
    for position in range(len(string) - 1):
        if string[position] == string[position + 1]:
            counter += 1
        else:
            compressed_string += f"{string[position]}{counter}"
            counter = 1
    compressed_string += f"{string[-1]}{counter}"

    if len(compressed_string) >= len(string):
        return string
    return compressed_string


test = "aaabbgggggggggggggggggggggggggggggggggcccctffg"

print(compress_str(test))
