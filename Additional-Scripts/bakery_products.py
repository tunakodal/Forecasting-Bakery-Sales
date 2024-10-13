import pandas as pd

df = pd.read_csv('bakery_sales.csv')

data_list = df['Items'].dropna().tolist()

uppercase_set = set()
lowercase_set = set()

# Iterate over each element and add it to the appropriate set
for element in data_list:
    if element[0].isupper():  # Starts with an uppercase letter
        uppercase_set.add(element)
    elif element[0].islower():  # Starts with a lowercase letter
        lowercase_set.add(element)

with open('names_output.txt', 'w') as file:
    file.write("Names starting with an uppercase letter:\n")
    for name in uppercase_set:
        file.write(f"{name}\n")

    file.write("\nNames starting with a lowercase letter:\n")
    for name in lowercase_set:
        file.write(f"{name}\n")

print("Names starting with an uppercase letter:", uppercase_set)
print("Names starting with a lowercase letter:", lowercase_set)

