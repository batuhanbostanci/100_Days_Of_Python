

with open("/Users/BATU/Desktop/Python-Projects/Day-24/Mail Merge Project/Input/Letters/starting_letter.txt") as data:
    text = data.read()


with open("/Users/BATU/Desktop/Python-Projects/Day-24/Mail Merge Project/Input/Names/invited_names.txt") as data:
    names_list = data.readlines()

for name in names_list:
    strip_name = name.strip()
    new_text = text.replace("[name]", strip_name)
    with open(f"Output/ReadyToSend/readyToSend{strip_name}.txt", mode="w") as file:
        file.write(new_text)


