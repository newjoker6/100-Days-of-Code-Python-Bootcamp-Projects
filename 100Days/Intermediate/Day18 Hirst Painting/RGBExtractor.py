import colorgram


colors = colorgram.extract("hirstspots.jpg", 40)

extracted_colour = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colour = (r, g, b)
    extracted_colour.append(new_colour)

del extracted_colour[0]
del extracted_colour[0]

colour_list = extracted_colour
