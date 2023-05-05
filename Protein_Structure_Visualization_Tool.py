from Bio.PDB import PDBParser

# Create a PDB parser object
parser = PDBParser() 

# Read in the PDB file and get the structure object
structure = parser.get_structure("protein", "4cri.pdb")

# Get the first model in the structure object
model = structure[0]

# Get the first chain in the model
chain = model['A']

# Get the coordinates of the alpha carbons in the chain
coords = []
for residue in chain:
    if residue.has_id('CA'):
        coords.append(residue['CA'].get_coord())


import pymol

# Initialize PyMOL
pymol.finish_launching()

# Load the PDB file into PyMOL
pymol.cmd.load("protein.pdb")

# Show the protein in cartoon representation
pymol.cmd.show_as("cartoon")

# Color the protein by chain
pymol.cmd.color("red", "chain A")
pymol.cmd.color("blue", "chain B")

# Zoom in on the protein
pymol.cmd.zoom("all")

# Save the image to a file
pymol.cmd.png("protein.png", width=800, height=600, dpi=300)

# Quit PyMOL
pymol.cmd.quit()
