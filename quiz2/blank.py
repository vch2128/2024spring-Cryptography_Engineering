# Open the original file for reading
with open('password.txt', 'r') as f:
    # Read the content of the file
    lines = f.readlines()

# Open the file for writing (this will overwrite the original file)
with open('blank.txt', 'w') as f:
    # Write the modified content back to the file
    for line in lines:
        # Add a space at the beginning of each line
        f.write(' ' + line)