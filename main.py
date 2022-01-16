sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆


word_list = sentence.split()

# print(word_list)
# print(len(word_list))

# result = {new_key: new_value for item in list}

result = {item: len(item) for item in sentence.split()}


print(result)

