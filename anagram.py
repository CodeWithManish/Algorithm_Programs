str_1 = input("Enter first string: ")
str_2 = input("Enter second string: ")


def check_anagram():
    if sorted(str_1) == sorted(str_2):
        return "string are Anagram"

    else:
        return "string are not Anagram"


if __name__ == '__main__':
    result = check_anagram()
    print(result)
