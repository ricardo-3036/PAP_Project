def LOAD_VERIFY(molecule):
    #Checks
    # 1.The provided molecule hasn’t been loaded yet.
    if molecule in loaded_molecules:

        print(f"Molecule {molecule} already loaded!")
        return
    # 2.The elements of all atoms are organic1.
    if not verify_organic_atoms(molecule):
        print(f"File {molecule} could not be loaded. Contains non-organic atom elements.")
        return

    # 3.Given the number nb of bonds in the header block, there are exactly nb bond lines.
    if not verify_bond_count(molecule):
        print(f"File {molecule} could not be loaded. Bonds block is incomplete.")
        return

    # 4.Given the number na of atoms in the header block, every atom appears at least once in the list bonds (bond block);
    if not verify_atoms_in_bonds(molecule):
        print(f"File {molecule} could not be loaded. Bonds block does not cover all atoms.")
        return
    
    # If all checks pass
    loaded_molecules.append(molecule)

    print(f"File {molecule} validated and loaded")


def LIST_MOLECULE(molecule):
    #When none
    if molecule not in loaded_molecules:
        print("No molecule loaded")
    
    #When at least 1 molecule is loaded
    else:
        print(f"Number of molecules loaded: {len(loaded_molecules)}")
        for mol in loaded_molecules:
            print(f" - {mol}")
        
def COUNT_ELEMENT(molecule, atom):
    #molecule is not loaded
    if molecule not in loaded_molecules:
        print(f"The molecule {molecule} is not loaded.")

    #molecule m is loaded and if the element is present in the molecule, it presents the atom count of that element
    if molecule in loaded_molecules and atom is verify_organic_atoms(molecule):

        count=count_atoms_in_molecule(molecule)

        print(f"The number of {atom} atom elements in the {molecule} molecule is {count}.")
    
    if count > 0:
        print(f"The number of {atom} atom elements in the {molecule} molecule is {count}.")
    
    else:
        print(f"The atom element {atom} does not exist in the {molecule} molecule.")
  
        
def D3_DISTANCE(molecule, atom, atom1, atom2):
    if molecule not in loaded_molecules:
        print(f"The molecule {molecule} is not loaded.")
    
    elif not molecule_has_3d_coordinates(molecule):
        print("Cannot compute the 3D distance. Coordinates are not available.")
        return

    distance = compute_3d_distance(molecule, atom1, atom2)  # Helper function
                
    if distance is not None:
        print(f"The 3D distance between atoms {atom1} and {atom2} of the {molecule} molecule is {round(distance, 2)}.")
    else:
        print("Invalid atom identifier provided.")


        
def FILTER_BY_ATOMS(atom):
    #Correct
    print("List of loaded molecules that meet the specified criteria:\n - {molecule1}...")
    #execution for a given k and atom A, where no molecule matches the criteria:
    print("No loaded molecule matches the criteria.")
    #execution for a given k with an invalid atom A:
    print("The provided atom is not part of the list of organic atoms.")
    #execution for a given k with and atom A, without molecules loaded:
    print("No molecules loaded.")
        
def TOP_BOND():


##HELPER FUNCTIONS

loaded_molecules=[]
verify_organic_atoms(molecule)
verify_bond_count(molecule)
verify_atoms_in_bonds(molecule)
count_atoms_in_molecule
molecule_has_3D_coordinates
compute_3d_distance