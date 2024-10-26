def count_elements(input_list):
    counts = {}
    for element in input_list:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts

# Example usage:
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
result = count_elements(my_list)
print(result)
