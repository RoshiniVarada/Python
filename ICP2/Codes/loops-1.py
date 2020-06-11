WeightLbs=[]
WeightKgs=[]
length=int(input("Enter the Number of Elements in List "))
for i in range(length):
    WeightLbs.append(float(input("Enter Number {} for List:".format(i+1))))
WeightKgs=[i*0.453592 for i in WeightLbs]
print("Weight Lbs: {}\nWeight Kgs: {}".format(WeightLbs,WeightKgs))
