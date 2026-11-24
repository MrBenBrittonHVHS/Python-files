shell_one = "The red ball"
shell_two = "The blue ball"
shell_three = "The green ball"
shell_one = shell_two
shell_two = shell_three
shell_one = "Nothing"
shell_three = shell_one
shell_one = shell_two 
shell_two = shell_three
print(f"{shell_one} is under shell one")
print(f"{shell_two} is under shell two")
print(f"{shell_three} is under shell three")