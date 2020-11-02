def find_substring(string, substring, index=-1):
    substring_index = string.find(substring, index + 1)
    return "" if substring_index < 0 else (str(substring_index) + " " + find_substring(string, substring, substring_index))

print(find_substring(input(), input()) or "-1")