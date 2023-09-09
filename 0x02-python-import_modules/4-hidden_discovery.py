#!bin/usr/python3
import dis

# Load the compiled module hidden_4.pyc
with open("hidden_4.pyc", "rb") as file:
    code = file.read()

# Disassemble the code
instructions = dis.get_instructions(code)

# Extract the names defined in the module
names = set()
for instruction in instructions:
    if instruction.opname == "LOAD_CONST":
        name = instruction.argval
        if isinstance(name, str) and not name.startswith("__"):
            names.add(name)

# Print the names in alphabetical order
for name in sorted(names):
    print(name)
