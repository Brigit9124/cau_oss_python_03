width = float(input("type width = "))
length = float(input("type length = "))
height = float(input("type height = "))

vol = width*length*height
print("Volume is ", vol)
total_length = length+width+height
if total_length <= 80:
    charge = 5000
elif total_length <= 100:
    charge = 8000
elif total_length <= 120:
    charge = 10000
elif total_length <= 160:
    charge = 13000
else:
    charge = "X"
print("total length is ", total_length)
print("\nCharge = ", charge) 
