# CHALLENGE ONE
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)

# CHALLENGE TWO
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [n for n in numbers if n % 2 == 0]
# print(result)

# CHALLENGE THREE
f = open("file1.txt", "r")
result = [int(n.strip('\n')) for n in f if n in open("file2.txt", "r")]
print(result)
