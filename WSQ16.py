a = open("93Cars.dat.txt", "r")

count_lines = 0
prices = 0.0
mpg_hw = 0.0
mpg_city = 0.0
for line in a:
    if(count_lines % 2 == 0):
        precio = line[42:46]
        precio = float(precio)
        prices = prices + precio

        hw = line[52:54]
        hw = float(hw)
        mpg_hw = mpg_hw + hw

        city = line[55:57]
        city = float(city)
        mpg_city = mpg_city + city

    count_lines = count_lines + 1

a.close()

k = (count_lines / 2)
y = (prices / k)
j = round (y,2)

o = (mpg_hw / count_lines)
p = round(o,2)

w = (mpg_city / count_lines)
t = round(w,2)

print("There are",count_lines,"lines.")
print("The total of prices is:", j)
print("The average of gas mileage on highway:",p)
print("The average of gas mileage on city:",t)
