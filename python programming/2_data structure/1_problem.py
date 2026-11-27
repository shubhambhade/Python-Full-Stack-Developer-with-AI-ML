# write a program to accept capital city name from the user and print the country name.

capital_cities = {
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "UK": "London",
    "Canada": "Ottawa",
    "Australia": "Canberra",
    "Japan": "Tokyo",
    "China": "Beijing",
    "Russia": "Moscow",
}

capital_city_name = input("Enter capital city name : ")


flag = False

for key , value in capital_cities.items():
    if capital_city_name.lower() == value.lower():
        print(f'{value} is capital of {key}')
        flag = True
        break

if flag == False:
    print("enter correct input")

