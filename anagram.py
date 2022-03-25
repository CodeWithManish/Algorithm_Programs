str_1 = input("Enter first string: ")
str_2 = input("Enter second string: ")


def check_anagram():
    if sorted(str_1) == sorted(str_2):
        print("string are Anagram")

    else:
        print("string are not Anagram")


if __name__ == '__main__':
    check_anagram()
