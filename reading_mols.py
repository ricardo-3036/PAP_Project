import os

class ReadingMols:

    def __init__(self, mol_file_path):
        
        #Initialize the class with the .mol file path and empty lists for atoms and bonds.
        # Path to the .mol file
        self.mol_file_path = mol_file_path
        # To store the name of the molecule
        self.molecule_name = ""  
        # List to store atom data
        self.atoms = []  
        # List to store bond data
        self.bonds = []  
        

    def read_mol_file_path(self, path):
        # Method to read the relevant info in the .mol files
        # If the .mol file doesnt exist
        if not os.path.exists(self.mol_file_path):
            return FileNotFoundError
        
        # Manually open the file
        file = open(self.mol_file_path, 'r')

        try: # Run the code we want to run
            # Read the lines
            lines = file.readlines()

        finally: # Ensures the closure of the file that was open, whether the code in the try block runs successfully or throws an error. 
            # Manually close the file
            file.close() 

        # Get molecule name from the first line
        self.molecule_name = lines[0].strip()

        # Extract atom and bond counts from the 4th line
        atom_count = int(lines[3].split()[0])  # Atom count
        bond_count = int(lines[3].split()[1])  # Bond count

        # Read atom data from the index 4 (line 5) until the last line on the atom_block
        for i in range(4, 4 + atom_count):
            # Split lines into parts
            parts=lines[i].split(" ")
            # Identify the index correlated to each coordinate
            x,y,z=float(parts[0]), float(parts[1]), float(parts[2])
            # Identify the element (O,C,...)
            element=parts[3]
            self.atoms.append({"element": element, "x": x, "y": y, "z":z})

        

        






