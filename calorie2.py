
calories = int(input("How Many Calories? "))
carbs = int(input("How Many Carbs? "))
fats = int(input("How Much Fat? "))
protein = int(input("How Much Protein? "))

def carbvalu(calories):
     carbval = calories/4  # type: int
     return carbval

carbval = carbvalu(calories)

#gram of carb is 4 calories
def carb(carbvalue, carbs):
     carb3 = carbs/carbvalue
     return carb3

carb3 = carb(carbval, carbs)
carb3 = carb3 * 100
carb3 = float("%.2f" % (carb3))      #use 2 decimal places
print("Percent of Carbs :", carb3)

##gram of fat is 9 calories

def fatvalu(calories):
     fatval = calories / 9
     return fatval

fatval = fatvalu(calories)       #define return fatval and call fatvalu function using calories


def fatcal(fatval2,fats):
     fatval2 = fats/fatval     #divide entered fats by calories per fat

     return fatval2
fatval2 = fatcal(fatval, fats)


fatval2= fatval2 * 100
fatval2 = float("%.2f" % (fatval2))
print("Percent of Fats: ", fatval2)

#gram of protein is 4 calories

def pro(carbval, protein):
     proteinCal = protein/carbval
     proteinCal = proteinCal * 100
     proteinCal = float("%.2f" %(proteinCal))
     print("Percent of Protein:", proteinCal)
     return proteinCal

pro(carbval, protein)
