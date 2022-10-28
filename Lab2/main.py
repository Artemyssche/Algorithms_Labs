def unpack():
    import re

    file = open("Lab2/resources/input.txt", "r")

    lines = file.readlines()

    color_picture = [line.split() for line in lines[3:]]

    number_extract_pattern = "\\d+"
    row_size, column_size = re.findall(number_extract_pattern, lines[0]) # returns ['10'], ['10']
    value_x, value_y = re.findall(number_extract_pattern, lines[1]) # returns ['3'] ['9']
    new_color_value = re.findall("[A-Z]", lines[2])[0] # returns ['C']

    return (int(value_x), int(value_y), 
            int(row_size), int(column_size), 
            str(new_color_value), color_picture)

row, column, width, height, color, img = unpack()

def flood_fill(picture, x, y, new_color):
    pixel_color = picture[x][y]
    queue = [(x, y)]
    visited = set()

    while len(queue) > 0:
        x, y = queue.pop(0)

        visited.add((x, y))

        if (picture[x][y] == pixel_color):
            picture[x][y] = new_color

        for x, y in neighbours(picture, x, y, pixel_color):
            if ((x, y) not in visited):
                queue.append((x, y))

    return picture

'''def test():
    pic = flood_fill(img, row, column, color)
    for i in range(width):
        for j in range(height):
            print(pic[i][j], end=' ')
        print()
        
    return 0

test()
'''

def neighbours(picture, x, y, pixel_color):
    variations = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    return [(x, y) for x, y in variations
            if (satisfies(picture, x, y, pixel_color))]


def satisfies(picture, x, y, pixel_color):
    return (0 <= x < width and
            0 <= y < height and 
            picture[x][y] == pixel_color)


if [line.split() for line in open("Lab2/resources/output.txt")] == flood_fill(img, row, column, color):
    for i in range(width):
        for j in range(height):
            print(img[i][j], end=' ')
        print()
    print("Life is good, because color fill equals to output.txt")

else:
    print("Bad, color fill doesn't equals to output.txt")