
# Key Error
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list =["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]


# Type Error
# a = "hello"
# print(a + 5)

# FileNotFound

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["dkjfkjdkf"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)            # This is different from java like if try is succeeded then else will start
# finally:
#     file.close()
#     print("The file was close ")
#     raise print("There is an error that i made up.")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError

bmi = weight/height **2

print(bmi)

