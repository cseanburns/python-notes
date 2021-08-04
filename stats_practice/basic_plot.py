import matplotlib.pyplot as plt

x = [590, 540, 740, 130, 810, 300, 320, 230, 470, 620, 770, 250]
y = [32, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]

# Marker style: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle
plt.scatter(x, y, s=60, c='red', marker='s')

plt.title("Relationship between Temp and Iced Coffee Sales")

plt.xlabel('Cups of Iced Coffee Sold')
plt.ylabel('Temperature in Fahrenheit')

plt.xlim(0,1000)
plt.ylim(0,100)

plt.show()
