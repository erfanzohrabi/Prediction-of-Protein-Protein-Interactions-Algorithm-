from Bio.PDB import PDBParser

# Create a PDB parser object
parser = PDBParser()

# Read in the PDB file and get the structure object
structure = parser.get_structure("protein", "protein.pdb")

# Get the first model in the structure object
model = structure[0]

# Get the first chain in the model
chain = model['A']

# Get the coordinates of the alpha carbons in the chain
coords = []
for residue in chain:
    if residue.has_id('CA'):
        coords.append(residue['CA'].get_coord())
