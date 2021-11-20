import os
import numpy as np
import matplotlib.colors as mcolors

from ase.io import read, write
from ase.visualize import view

#from ase.data import atomic_numbers, chemical_symbols
#from asap3.analysis.rdf import RadialDistributionFunction

from collections import Counter

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

from ClusterGeoFigures.No_Of_Neighbours import No_Of_Neighbours

class ClusterGeoFigures_Program:
	def __init__(self, r_cut, elements=['Cu','Pd'],path_to_here='.'):
		self.path_to_here = os.path.abspath(path_to_here)
		self.r_cut = r_cut
		self.elements = elements
		self.run()

	def run(self):
		print('--------------------------------------')
		print('Getting data from XYZ files')
		clusters_data = self.get_cluster_data()
		print('Finished getting data from XYZ files')
		print('--------------------------------------')
		print('Analysing data')
		cluster_information = self.analyse_cluster_data(clusters_data)
		print('Finished analysing data')
		print('--------------------------------------')
		print('Making plots')
		self.make_plots(cluster_information)
		print('Finished making plots')
		print('--------------------------------------')

	def get_cluster_data(self):
		clusters_data = {}
		for file in os.listdir(self.path_to_here):
			if not file.endswith('.xyz'):
				continue
			cluster = read(self.path_to_here+'/'+file)
			clusters_data.setdefault(len(cluster),[]).append((cluster,file))
		self.greatest_no_of_atoms = max(clusters_data.keys())
		clusters_data_temp = clusters_data[self.greatest_no_of_atoms]
		clusters_data = {}
		for cluster, file in clusters_data_temp:
			symbols = cluster.get_chemical_symbols()
			no_of_symbols = Counter(symbols)
			name = ''.join([element+str(no_of_symbols[element]) for element in self.elements])+'.xyz'
			name = name.lower()
			if not name.lower() == file.lower():
				continue
			clusters_data[tuple([no_of_symbols[element] for element in self.elements])] = cluster
		return clusters_data

	def analyse_cluster_data(self,clusters_data):
		cluster_information = self.analyse_NN_1(clusters_data)
		return cluster_information

	def analyse_NN_1(self, clusters_data):
		cluster_information = {}
		for key in sorted(clusters_data.keys()):
			cluster = clusters_data[key]
			nl = No_Of_Neighbours([self.r_cut/2.0]*len(cluster))
			nl.update(cluster)
			all_number_of_neighbours = {}
			Cu_number_of_neighbours = {}
			for index in range(len(cluster)):
				indices, offsets = nl.get_neighbors(index)
				number_of_neighbours = len(indices)
				all_number_of_neighbours.setdefault(number_of_neighbours,[]).append(index)
				if cluster[index].symbol == 'Cu':
					Cu_number_of_neighbours.setdefault(number_of_neighbours,[]).append(index)
			cluster_information[key] = (Cu_number_of_neighbours, all_number_of_neighbours, cluster)
			#import pdb; pdb.set_trace()
		return cluster_information

	def make_plots(self, cluster_information):
		cluster_information = [(key, Cu_number_of_neighbours, all_number_of_neighbours, cluster) for key, (Cu_number_of_neighbours, all_number_of_neighbours, cluster) in cluster_information.items()]
		cluster_information.sort()
		no_of_copper_atoms = []
		bulk_data   = [] # 12+ neighbours
		face_data   = [] # 9-11 neighbours
		edge_data   = [] # 7-8 neighbours
		vertex_data = [] # <= 6 nieghbours
		for key, Cu_number_of_neighbours, all_number_of_neighbours, cluster in cluster_information:
			no_of_Cu_atoms_in_cluster = key[self.elements.index('Cu')]
			no_of_copper_atoms.append(no_of_Cu_atoms_in_cluster)
			# ---------------------------------------------------------------------
			Cu_bulk = Cu_face = Cu_edge = Cu_vertex = 0
			for number_of_neighbours, indices in Cu_number_of_neighbours.items():
				if number_of_neighbours >= 12:
					Cu_bulk += len(indices)
				elif 9 <= number_of_neighbours <= 11:
					Cu_face += len(indices)
				elif 7 <= number_of_neighbours <= 8:
					Cu_edge += len(indices)
				elif number_of_neighbours <= 6:
					Cu_vertex += len(indices)
				else:
					exit('Huh?')
			# ---------------------------------------------------------------------
			bulk = face = edge = vertex = 0
			for number_of_neighbours, indices in all_number_of_neighbours.items():
				if number_of_neighbours >= 12:
					bulk += len(indices)
				elif 9 <= number_of_neighbours <= 11:
					face += len(indices)
				elif 7 <= number_of_neighbours <= 8:
					edge += len(indices)
				elif number_of_neighbours <= 6:
					vertex += len(indices)
				else:
					exit('Huh?')
			# ---------------------------------------------------------------------
			percent_bulk = (Cu_bulk/bulk)*100.0 if not bulk == 0 else -50.0
			percent_face = (Cu_face/face)*100.0 if not face == 0 else -50.0
			percent_edge = (Cu_edge/edge)*100.0 if not edge == 0 else -50.0
			percent_vertex = (Cu_vertex/vertex)*100.0 if not vertex == 0 else -50.0
			# ---------------------------------------------------------------------
			print('no_of_Cu_atoms_in_cluster: '+str(no_of_Cu_atoms_in_cluster))
			print('Cu_bulk: '+str(Cu_bulk)+'; bulk: '+str(bulk)+': Percent: '+str(percent_bulk))
			print('Cu_face: '+str(Cu_face)+'; face: '+str(face)+': Percent: '+str(percent_face))
			print('Cu_edge: '+str(Cu_edge)+'; edge: '+str(edge)+': Percent: '+str(percent_edge))
			print('Cu_vertex: '+str(Cu_vertex)+'; vertex: '+str(vertex)+': Percent: '+str(percent_vertex))
			print('--------------------')
			# ---------------------------------------------------------------------
			bulk_data.append(percent_bulk)
			face_data.append(percent_face)
			edge_data.append(percent_edge)
			vertex_data.append(percent_vertex)
			#import pdb; pdb.set_trace()
		figure(figsize=(8, 3), dpi=80)
		plt.plot([0, self.greatest_no_of_atoms], [0, 100], c='k', ls='-', lw=2.0)
		plt.scatter(no_of_copper_atoms,vertex_data,c='green')
		plt.scatter(no_of_copper_atoms,edge_data,c='blue')
		plt.scatter(no_of_copper_atoms,face_data,c='red')
		plt.scatter(no_of_copper_atoms,bulk_data,c=(255/255.0, 20/255.0, 147/255.0))
		plt.xlabel('$\mathregular{N_{Cu}}$')
		plt.ylabel('% Cu composition')
		plt.ylim((-0.5,100.5))
		plt.xlim((0-1,self.greatest_no_of_atoms+1))
		plt.tight_layout()
		plt.savefig('percent_Cu_comp_vs_no_Cu_atoms.png')