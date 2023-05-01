import sys


def convert_isbn_10_to_13(isbn10):
    isbn13 = "978" + isbn10[:len(isbn10) - 1]
    check_digit = calculate_isbn13_checksum(isbn13) % 10
    if check_digit > 0:
        check_digit = 10 - check_digit

    return isbn13 + str(check_digit)


def is_valid_isbn13(isbn):
    if len(isbn) != 13:
        return False
    return calculate_isbn13_checksum(isbn) % 10 == 0


def calculate_isbn13_checksum(isbn):
    sum = 0
    multipliers = [1, 3]
    for i in range(len(isbn)):
        sum = sum + eval(isbn[i]) * (multipliers[i % 2])

    return sum


def is_valid_isbn10(isbn):
    if len(isbn) != 10:
        return False

    sum = 0
    for i in range(len(isbn) - 1):
        sum = sum + eval(isbn[i]) * (len(isbn) - i)

    if isbn[len(isbn) - 1].upper() == 'X':
        sum = sum + 10
    else:
        sum = sum + eval(isbn[len(isbn) - 1])

    return sum % 11 == 0


def validate_isbn(isbn):
    if is_valid_isbn13(isbn):
        return "Valid"

    if is_valid_isbn10(isbn):
        return convert_isbn_10_to_13(isbn)

    return "Invalid"


def test_valid_isbn():
    isbn13_valid = ["9892879138714", "9780316066525", "9892879225629", "9892837055923"]
    for isbn in isbn13_valid:
        assert validate_isbn(isbn) == "Valid", "{} is a Valid ISBN-13 code.".format(isbn)

    isbn13_invalid = ["989289138714", "0330301824", "989287225629", "9892835923"]
    for isbn in isbn13_invalid:
        assert validate_isbn(isbn) == "Invalid", "{} is an Invalid ISBN-13 code.".format(isbn)

    isbn10_valid = [["0316066524", "9780316066525"], ["0136091814", "9780136091813"]]
    for isbn in isbn10_valid:
        assert validate_isbn(isbn[0]) == isbn[1], "{} is a Valid ISBN-10 code.".format(isbn[0])

    isbn10_invalid = [["0136091815", "Invalid"], ["013609181X", "Invalid"]]
    for isbn in isbn10_invalid:
        assert validate_isbn(isbn[0]) == isbn[1], "{} is an Invalid ISBN-10 code.".format(isbn[0])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit()

    if sys.argv[1].lower() == 'test':
        test_valid_isbn()
        print("All tests passed.")
        exit()

    print(validate_isbn(sys.argv[1]))
