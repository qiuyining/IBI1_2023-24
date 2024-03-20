#  store population sizes for cities in the UK 
uk_cities = [0.56, 0.62, 0.04, 9.7]
#  store population sizes for cities in China
china_cities = [0.58, 8.4, 29.9, 22.2]
# Sort the lists
uk_cities_sorted = sorted(uk_cities)
china_cities_sorted = sorted(china_cities)
print("Sorted UK Cities Populations:", uk_cities_sorted)
print("Sorted China Cities Populations:", china_cities_sorted)
# import pyplot function from matplotlib
import matplotlib.pyplot as plt
# name the label
uk_cities_names=["Edinburgh","Glasgow","Stirling","London"]
width = 0.5
# create the bar plot for cities in the UK 
plt.figure
plt.bar(uk_cities_names,uk_cities,width=width,color='red')
plt.xlabel('City')
plt.ylabel("Population(millions)")
plt.title("City Size in UK")
# show the bar plot
plt.show()
# close the bar plot
plt.clf()
china_cities_names=["Haining","hangzhou","Shanghai","Beijing"]
width = 0.5
# create the bar plot for cities in China
plt.figure
plt.bar(china_cities_names,china_cities,width=width,color='green')
plt.xlabel('City')
plt.ylabel("Population(millions)")
plt.title("City Size in China")
# show the bar plot
plt.show()
# close the bar plot
plt.clf()