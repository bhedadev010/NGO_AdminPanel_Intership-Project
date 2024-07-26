
#TASK 1
grocery = ["milk","eggs","bread","butter"]
length = len(grocery)

i=2
if grocery[i] in grocery:
  print(f"{grocery[i]} exists")

else:
  print(f"{grocery[i]} does not exist")

#TASK 2
movie =["Kalki","Oppenheimer","Article 370","Animal"]
i=3
print(f"{movie[i]} is 3rd index")

listcom=movie+grocery
print(listcom)