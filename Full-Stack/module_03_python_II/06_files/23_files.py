# CREATE and WRITE in FILES

"""
files usually are used for log data

open() -> allows us to create or open files. If the file existed, open it,
If the file did not exist, create it

w+ -> allows us to write to the file
"""

# create or open a file
file_builder = open("directory_1/directory_1B/logger.txt", "w+")

# write in the file
file_builder.write("Hey, I'm in a file!")

# close the file
file_builder.close()



# ANTOHER EXAMPLE
# it will delete what is written before in the file because we are using 'w+'.
file_builder = open("directory_1/directory_1B/logger.txt", "w+")

for i in range(100):
    file_builder.write(f"I'm on line {i + 1}\n")

file_builder.close()