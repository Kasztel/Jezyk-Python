lenght = input("Podaj długość: ")
height = input("Podaj wysokość: ")

num_lenght = int(lenght)
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

print(square)
