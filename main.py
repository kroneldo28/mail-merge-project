# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

# Let's store the names in a list
with open("Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

for name in names:
    with open("Input/Letters/starting_letter.txt", "r") as sample_letter:
        new_letter = sample_letter.readlines()
    with open(f"Output/ReadyToSend/letter_to_{name}.txt", "w") as final_letter:
        for each_line in new_letter:
            each_line = each_line.replace(PLACEHOLDER, name.strip())
            final_letter.write(each_line)


