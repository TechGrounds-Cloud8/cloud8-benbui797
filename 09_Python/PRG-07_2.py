list = [9, 80, 16, 67, 35]

print(f"My list: {list}")

# enumerate adds a number (the index) to every element in the list. 
# you have to assign a variable to both elements (in this case i and j)
# it is useful in this situation, but range gives more flexibility (you can define start, stop and step)

for i, j in enumerate(list):
    # print(f"{i=} {j=}")                   # uncomment this to see the values of i and j printed out!

    if i == len(list) - 1:
        print(j + list[0])
    else:
        print(j + list[i + 1])
