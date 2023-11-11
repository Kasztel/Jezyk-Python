def ruler(n):
    dots = "...."
    vertical = "|"

    length = int(n)
    output = ""
    # creating output string
    for i in range(0, length):
        output += vertical + dots
    output += vertical + "\n"

    for k in range(0, length):
        output += str(k) + (" " * (5 - len(str(k + 1))))

    output += str(n)

    return output


def grid(length, height):
    num_lenght = int(length)
    num_height = int(height) + 1

    horizontal_piece = "+---"
    vertical_piece = "|"

    horizontal_connector = ""
    vertical_connector = ""
    square = ""

    for i in range(0, num_lenght):
        horizontal_connector += horizontal_piece
    horizontal_connector += "+\n"

    for j in range(0, num_lenght):
        vertical_connector += vertical_piece + " " * 3
    vertical_connector += "|\n"

    for k in range(0, num_height - 1):
        square += horizontal_connector + vertical_connector
    square += horizontal_connector

    return square


ruler_input = input("ruller length: ")
print(ruler(ruler_input))

lenght_input = input("length of grid: ")
height_input = input("height of grid: ")

print(grid(lenght_input, height_input))
