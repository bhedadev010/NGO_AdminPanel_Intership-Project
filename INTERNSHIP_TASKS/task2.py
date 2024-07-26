#TASK 1

list1 = ["milk", "eggs", "bread", "butter"]
list1.append("dev")
print(list1)
list1.remove(list1[3])
print(list1)
list1.pop()
print(list1)
list1.insert(1, "cheese")
print(list1)
list1.sort()
print(list1)
n = len(list1)
print(n)
list1.append("eggs")
m = list1.count("eggs")
print(m)


#TASK 2

mydata = [{"states":["GUJARAT","RAJASTHAN",{"PORTION":"WEST INDIA"},{"LANGUAGES":["GUJARATI","MARWADI",["HINDI","ENGLISH"]]}]},
{"CODES":{"GUJARAT":"GJ","RAJASTHAN":"RJ"}},["7.07 CR","8.5CR"]];

print(mydata[1]["CODES"]["GUJARAT"])

print(mydata[0]["states"][3]["LANGUAGES"][1])

print(mydata[0]["states"][3]["LANGUAGES"][2][1])

print(mydata[0]["states"][2]["PORTION"])

print(mydata[2][0])


#TASK 3

mydata = {"maharashtra":{"mumbai":{"city":"metro city","metro":"yes"},"population":"20 cr"},
"gujarat": ["AHMEDABAD","SURAT","RAJKOT"],
"rajasthan":["AJMER","JAISALMER",{"capital":"jaipur"},["MEWAD","RJ","INR"]]
}

print(mydata.keys())

n = len(mydata.keys())
print(n)

print(mydata["maharashtra"]["mumbai"]["city"])

print(mydata['rajasthan'][2]['capital'])

print(mydata["gujarat"][2])

print(mydata["rajasthan"][3][1])
