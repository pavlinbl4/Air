outer = [ [1,2,3], [4,[25,44],6], [7,8,9]]

# outer = [1, 2, 3, 4, [25, 44], 6, 7, 8, 9]

new_list = [item for sublist in outer for item in sublist]
print(new_list)