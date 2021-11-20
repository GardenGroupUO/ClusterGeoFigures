
class No_Of_Neighbours:
	def __init__(self, bond_radii):
		self.bond_radii = bond_radii

	def update(self, cluster):
		no_of_atoms = len(cluster)
		self.no_of_neighbours = {atom_index: [] for atom_index in range(no_of_atoms)}
		for atom_index in range(no_of_atoms):
			atom_1_radius = self.bond_radii[atom_index]
			for other_atom_index in range(atom_index+1, no_of_atoms):
				#if other_atom_index == atom_index:
				#	continue
				atom_2_radius = self.bond_radii[atom_index]
				max_bonding_distance = atom_1_radius + atom_2_radius
				length = cluster.get_distance(atom_index,other_atom_index)
				if length <= max_bonding_distance:
					self.no_of_neighbours[atom_index].append(other_atom_index)
					self.no_of_neighbours[other_atom_index].append(atom_index)

	def get_neighbors(self, atom_index):
		return self.no_of_neighbours[atom_index], None