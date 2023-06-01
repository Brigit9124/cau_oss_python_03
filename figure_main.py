import figure.py

myline = figure.line(10,20)

width, height = myline.get_length()
try :
    rectangle = figure.area_rectangle(width,height)
    print(rectangle)
except ValueError:
    print("Error")
    