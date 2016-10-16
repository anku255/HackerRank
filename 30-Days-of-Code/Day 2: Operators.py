"""Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost."""

#Taking input for mealCost, tipPercent and taxPercent

mealCost = float(raw_input())
tipPercent = int(raw_input())
taxPercent = int(raw_input())

#Calculating totalCost
totalCost = mealCost + (mealCost*tipPercent/100) + (mealCost*taxPercent/100)

#rounding off totolCost
totalCost = int(round(totalCost))

#printing final result
print "The total meal cost is " + str(totalCost) + " dollars."
