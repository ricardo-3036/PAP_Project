
# Import soul of the commands to this file
from commands import LOAD_VERIFY, LIST_MOLECULE, COUNT_ELEMENT, D3_DISTANCE, FILTER_BY_ATOMS, TOP_BOND


# Receive the initial string and split it into a command and the molecule
def initial_string_split():
    command_to_execute=input("Command to execute: ")

    command, molecule=command_to_execute.split(" ")

    command=command.upper()
    molecule=molecule.lower()

    return command, molecule


# Loop the possible commands 
def execute_command():

    command, molecule=initial_string_split()

    while command!="EXIT":
        if command=="LOAD_VERIFY":
            LOAD_VERIFY(molecule)

        elif command=="LIST_MOLECULE":
            LIST_MOLECULE()

        elif command=="COUNT_ELEMENT":
            COUNT_ELEMENT(molecule)

        elif command=="3D_DISTANCE":
            D3_DISTANCE(molecule)

        elif command=="FILTER_BY_ATOMS":
            FILTER_BY_ATOMS()

        elif command=="TOP_BOND":
            TOP_BOND()

        else:
            print("UNKNOWN_COMMAND")

        command, molecule=initial_string_split()

    print("Goodbye!")
