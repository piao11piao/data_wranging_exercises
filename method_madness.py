# splitting a string "literal" and then printing the result
split_world = "Hello world".split()
print(split_world)

# assigning a string to a variable
# then printing the result of calling the split() methos on it
world_msg = "Hello World"
print(world_msg.split())

# Error: the split() method must be calles on a string
split("Hello World")

# there is no split() method for numbers
print(5.split())
