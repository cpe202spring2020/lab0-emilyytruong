def weight_on_planets():
   earth_weight = float(input("What do you weigh on earth? "))
   mars = earth_weight * 0.38
   jupiter = earth_weight * 2.34
   print("\nOn Mars you would weigh", round(mars, 2), "pounds.","\nOn Jupiter you would weigh", round(jupiter, 2), "pounds.")

   
   
if __name__ == '__main__':
   weight_on_planets()
