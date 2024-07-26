#TASK 1

cart = {
"Laptop": {
"price": 1000,
"quantity": 1,
"categories": ["Electronics", "Computers"],
"manufacturer": "TechCorp",
"reviews": [{"user": "Alice", "rating": 5}, {"user": "Bob", "rating": 4.5}]
},
"Mouse": {
"price": 50,
"quantity": 2,
"categories": ["Electronics", "Accessories"],
"manufacturer": "GadgetPro",
"reviews": [{"user": "Charlie", "rating": 4}, {"user": "Dave", "rating": 4.5}]
},
  "Keyboard": {
  "price": 80,
  "quantity": 1,
  "categories": ["Electronics", "Accessories"],
  "manufacturer": "GadgetPro",
  "reviews": [{"user": "Eve", "rating": 4.5}, {"user": "Frank", "rating": 4}]
  },
  "Headphones": {
  "price": 200,
  "quantity": 1,
  "categories": ["Electronics", "Audio"],
  "manufacturer": "SoundMax",
  "reviews": [{"user": "Grace", "rating": 5}, {"user": "Heidi", "rating": 4.8}]
  }
  }

n=len(cart.keys())
print(n)

#question 2, answer not found

print(cart.values())

print(cart["Keyboard"]["categories"])

#question 5, question not clear but answer,
print(cart["Headphones"]["manufacturer"])

print(len(cart["Keyboard"]["reviews"]))

print(cart["Laptop"]["reviews"][0]["rating"])
print(cart["Laptop"]["reviews"][1]["rating"])
print(cart["Mouse"]["reviews"][0]["rating"])
print(cart["Mouse"]["reviews"][1]["rating"])
print(cart["Keyboard"]["reviews"][0]["rating"])
print(cart["Keyboard"]["reviews"][1]["rating"])
print(cart["Headphones"]["reviews"][0]["rating"])
print(cart["Headphones"]["reviews"][1]["rating"])

n= ((cart["Mouse"]["reviews"][0]["rating"])+(cart["Mouse"]["reviews"][1]["rating"]))/2
print(n)
