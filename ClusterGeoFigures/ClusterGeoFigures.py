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

from openpyxl import Workbook
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment

class ClusterGeoFigures_Program:
	def __init__(self, r_cut, elements=['Cu','Pd'],focus_plot_with_respect_to_element='Cu',path_to_here='.',add_legend=False):
		self.path_to_here = os.path.abspath(path_to_here)
		self.r_cut = r_cut
		self.elements = elements
		self.focus_plot_with_respect_to_element = focus_plot_with_respect_to_element
		self.add_legend = add_legend

		self.to_save = []
		self.to_save += [str(self.focus_plot_with_respect_to_element)+'_bulk'  ,'bulk'  ,str(self.focus_plot_with_respect_to_element)+'_percent_bulk']
		self.to_save += [str(self.focus_plot_with_respect_to_element)+'_face','face'  ,str(self.focus_plot_with_respect_to_element)+'_percent_face']
		self.to_save += [str(self.focus_plot_with_respect_to_element)+'_edge'  ,'edge'  ,str(self.focus_plot_with_respect_to_element)+'_percent_edge']
		self.to_save += [str(self.focus_plot_with_respect_to_element)+'_vertex','vertex',str(self.focus_plot_with_respect_to_element)+'_percent_vertex']

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
		cluster_plot_data = self.make_plots(cluster_information)
		print('Finished making plots')
		print('--------------------------------------')
		print('Making excel spreadsheet')
		self.record_to_excel(cluster_plot_data)
		print('Finished excel spreadsheet')
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
			element_number_of_neighbours = {}
			for index in range(len(cluster)):
				indices, offsets = nl.get_neighbors(index)
				number_of_neighbours = len(indices)
				all_number_of_neighbours.setdefault(number_of_neighbours,[]).append(index)
				if cluster[index].symbol == self.focus_plot_with_respect_to_element:
					element_number_of_neighbours.setdefault(number_of_neighbours,[]).append(index)
			cluster_information[key] = (element_number_of_neighbours, all_number_of_neighbours, cluster)
		return cluster_information

	def make_plots(self, cluster_information_overall):
		cluster_information = [(key, element_number_of_neighbours, all_number_of_neighbours, cluster) for key, (element_number_of_neighbours, all_number_of_neighbours, cluster) in cluster_information_overall.items()]
		cluster_information.sort()
		cluster_plot_data = {}
		no_of_copper_atoms = []

		bulk_data   = [] # 12+ neighbours
		face_data   = [] # 9-11 neighbours
		edge_data   = [] # 7-8 neighbours
		vertex_data = [] # <= 6 nieghbours

		max_bulk_data   = [] # 12+ neighbours
		max_face_data   = [] # 9-11 neighbours
		max_edge_data   = [] # 7-8 neighbours
		max_vertex_data = [] # <= 6 nieghbours
		
		norm_bulk_data   = [] # 12+ neighbours
		norm_face_data   = [] # 9-11 neighbours
		norm_edge_data   = [] # 7-8 neighbours
		norm_vertex_data = [] # <= 6 nieghbours
		for key, element_number_of_neighbours, all_number_of_neighbours, cluster in cluster_information:
			no_of_element_atoms_in_cluster = key[self.elements.index(self.focus_plot_with_respect_to_element)]
			no_of_copper_atoms.append(no_of_element_atoms_in_cluster)
			# ---------------------------------------------------------------------
			element_bulk = element_face = element_edge = element_vertex = 0
			for number_of_neighbours, indices in element_number_of_neighbours.items():
				if number_of_neighbours >= 12:
					element_bulk += len(indices)
				elif 9 <= number_of_neighbours <= 11:
					element_face += len(indices)
				elif 7 <= number_of_neighbours <= 8:
					element_edge += len(indices)
				elif number_of_neighbours <= 6:
					element_vertex += len(indices)
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
			element_percent_bulk   = (element_bulk/bulk)*100.0     if not bulk == 0 else -50.0
			element_percent_face   = (element_face/face)*100.0     if not face == 0 else -50.0
			element_percent_edge   = (element_edge/edge)*100.0     if not edge == 0 else -50.0
			element_percent_vertex = (element_vertex/vertex)*100.0 if not vertex == 0 else -50.0
			# ---------------------------------------------------------------------
			print('no_of_'+str(self.focus_plot_with_respect_to_element)+'_atoms_in_cluster: '+str(no_of_element_atoms_in_cluster))
			print(str(self.focus_plot_with_respect_to_element)+'_bulk: '+str(element_bulk)+'; bulk: '+str(bulk)+': Percent: '+str(element_percent_bulk))
			print(str(self.focus_plot_with_respect_to_element)+'_face: '+str(element_face)+'; face: '+str(face)+': Percent: '+str(element_percent_face))
			print(str(self.focus_plot_with_respect_to_element)+'_edge: '+str(element_edge)+'; edge: '+str(edge)+': Percent: '+str(element_percent_edge))
			print(str(self.focus_plot_with_respect_to_element)+'_vertex: '+str(element_vertex)+'; vertex: '+str(vertex)+': Percent: '+str(element_percent_vertex))
			print('--------------------')
			# ---------------------------------------------------------------------
			bulk_data.append(element_bulk if bulk > 0 else -50)
			face_data.append(element_face if face > 0 else -50)
			edge_data.append(element_edge if edge > 0 else -50)
			vertex_data.append(element_vertex if vertex > 0 else -50)

			max_bulk_data.append(bulk if bulk > 0 else -50)
			max_face_data.append(face if face > 0 else -50)
			max_edge_data.append(edge if edge > 0 else -50)
			max_vertex_data.append(vertex if vertex > 0 else -50)
			
			norm_bulk_data.append(element_percent_bulk)
			norm_face_data.append(element_percent_face)
			norm_edge_data.append(element_percent_edge)
			norm_vertex_data.append(element_percent_vertex)
			# ---------------------------------------------------------------------
			cluster_plot_data[key] = {}
			for data_name in self.to_save:
				if self.focus_plot_with_respect_to_element in data_name:
					getting_data_name = data_name.replace(self.focus_plot_with_respect_to_element,'element')
				else:
					getting_data_name = data_name
				cluster_plot_data[key][data_name] = eval(getting_data_name)
			# ---------------------------------------------------------------------

		# -------------------------------------------------------------------------
		# normalised percents of elements in positions in cluster
		figure(figsize=(8, 3), dpi=80)
		plt.plot([0, self.greatest_no_of_atoms], [0, 100], c='k', ls='-', lw=2.0)
		plt.scatter(no_of_copper_atoms,norm_vertex_data,c='green',label='vertex')
		plt.scatter(no_of_copper_atoms,norm_edge_data,c='blue',label='edge')
		plt.scatter(no_of_copper_atoms,norm_face_data,c='red',label='face')
		plt.scatter(no_of_copper_atoms,norm_bulk_data,c=(255/255.0, 20/255.0, 147/255.0),label='bulk')
		plt.xlabel('$\mathregular{N_{'+str(self.focus_plot_with_respect_to_element)+'}}$')
		plt.ylabel('Normalised % '+str(self.focus_plot_with_respect_to_element)+' composition')
		plt.ylim((-0.5,100.5))
		plt.xlim((0-1,self.greatest_no_of_atoms+1))
		plt.tight_layout()
		if self.add_legend:
			plt.legend()
		name_of_file = 'normalised_percent_'+str(self.focus_plot_with_respect_to_element)+'_comp_vs_no_'+str(self.focus_plot_with_respect_to_element)+'_atoms'
		plt.savefig(name_of_file+'.png')
		plt.savefig(name_of_file+'.svg')

		# --------------

		fig = figure(figsize=(8, 6), dpi=80)
		ax = fig.add_subplot(111)    # The big subplot
		ax1 = fig.add_subplot(221)
		ax2 = fig.add_subplot(222)
		ax3 = fig.add_subplot(223)
		ax4 = fig.add_subplot(224)

		# Turn off axis lines and ticks of the big subplot
		ax.spines['top'].set_color('none')
		ax.spines['bottom'].set_color('none')
		ax.spines['left'].set_color('none')
		ax.spines['right'].set_color('none')
		ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

		for axis in [ax1, ax2, ax3, ax4]:
			axis.plot([0, self.greatest_no_of_atoms], [0, 100], c='k', ls='-', lw=2.0,zorder=-10)
			axis.set_ylim((-0.5,100.5))
			axis.set_xlim((0-1,self.greatest_no_of_atoms+1))

		ax4.scatter(no_of_copper_atoms,norm_vertex_data,c='green',label='vertex')
		ax3.scatter(no_of_copper_atoms,norm_edge_data,c='blue',label='edge')
		ax2.scatter(no_of_copper_atoms,norm_face_data,c='red',label='face')
		ax1.scatter(no_of_copper_atoms,norm_bulk_data,c=(255/255.0, 20/255.0, 147/255.0),label='bulk')

		ax.set_xlabel('$\mathregular{N_{'+str(self.focus_plot_with_respect_to_element)+'}}$')
		ax.set_ylabel('Normalised % '+str(self.focus_plot_with_respect_to_element)+' composition')

		plt.tight_layout()
		if self.add_legend:
			for axis in [ax1, ax2, ax3, ax4]:
				axis.legend()
		name_of_file = name_of_file+'_subplots'
		plt.savefig(name_of_file+'.png')
		plt.savefig(name_of_file+'.svg')

		# -------------------------------------------------------------------------
		# -------------------------------------------------------------------------
		# no of elements in positions in cluster, with maximum number of those positions.
		# given as the number of atoms
		figure(figsize=(8, 3), dpi=80)

		plt.scatter(no_of_copper_atoms,max_vertex_data,edgecolors='green', c='white', linewidths=2,label='max vertex')
		plt.scatter(no_of_copper_atoms,max_edge_data,edgecolors='blue', c='white', linewidths=2,label='max edge')
		plt.scatter(no_of_copper_atoms,max_face_data,edgecolors='red', c='white', linewidths=2,label='max face')
		plt.scatter(no_of_copper_atoms,max_bulk_data,edgecolors=(255/255.0, 20/255.0, 147/255.0), c='white', linewidths=2,label='max bulk')

		plt.scatter(no_of_copper_atoms,vertex_data,c='green',label='vertex')
		plt.scatter(no_of_copper_atoms,edge_data,c='blue',label='edge')
		plt.scatter(no_of_copper_atoms,face_data,c='red',label='face')
		plt.scatter(no_of_copper_atoms,bulk_data,c=(255/255.0, 20/255.0, 147/255.0),label='bulk')

		plt.xlabel('$\mathregular{N_{'+str(self.focus_plot_with_respect_to_element)+'}}$')
		plt.ylabel('# '+str(self.focus_plot_with_respect_to_element)+' atoms composition')
		plt.ylim((-0.5,self.greatest_no_of_atoms+.5))
		plt.xlim((0-1,self.greatest_no_of_atoms+1))		
		plt.tight_layout()
		if self.add_legend:
			for axis in [ax1, ax2, ax3, ax4]:
				axis.legend()
		name_of_file = 'no_of_'+str(self.focus_plot_with_respect_to_element)+'_comp_vs_no_'+str(self.focus_plot_with_respect_to_element)+'_atoms'
		plt.savefig(name_of_file+'.png')
		plt.savefig(name_of_file+'.svg')

		# --------------

		fig = figure(figsize=(8, 6), dpi=80)
		ax = fig.add_subplot(111)    # The big subplot
		ax1 = fig.add_subplot(221)
		ax2 = fig.add_subplot(222)
		ax3 = fig.add_subplot(223)
		ax4 = fig.add_subplot(224)

		# Turn off axis lines and ticks of the big subplot
		ax.spines['top'].set_color('none')
		ax.spines['bottom'].set_color('none')
		ax.spines['left'].set_color('none')
		ax.spines['right'].set_color('none')
		ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

		for axis in [ax1, ax2, ax3, ax4]:
			axis.plot([0, self.greatest_no_of_atoms], [0, 100], c='k', ls='-', lw=2.0,zorder=-10)
			axis.set_ylim((-0.5,100.5))
			axis.set_xlim((0-1,self.greatest_no_of_atoms+1))

		ax4.scatter(no_of_copper_atoms,max_vertex_data,edgecolors='green', c='white', linewidths=2,label='max vertex')
		ax3.scatter(no_of_copper_atoms,max_edge_data,edgecolors='blue', c='white', linewidths=2,label='max edge')
		ax2.scatter(no_of_copper_atoms,max_face_data,edgecolors='red', c='white', linewidths=2,label='max face')
		ax1.scatter(no_of_copper_atoms,max_bulk_data,edgecolors=(255/255.0, 20/255.0, 147/255.0), c='white', linewidths=2,label='max bulk')

		ax4.scatter(no_of_copper_atoms,vertex_data,c='green',label='vertex')
		ax3.scatter(no_of_copper_atoms,edge_data,c='blue',label='edge')
		ax2.scatter(no_of_copper_atoms,face_data,c='red',label='face')
		ax1.scatter(no_of_copper_atoms,bulk_data,c=(255/255.0, 20/255.0, 147/255.0),label='bulk')

		ax.set_xlabel('$\mathregular{N_{'+str(self.focus_plot_with_respect_to_element)+'}}$')
		ax.set_ylabel('Normalised % '+str(self.focus_plot_with_respect_to_element)+' composition')

		plt.tight_layout()
		#if self.add_legend:
		#	for axis in [ax1, ax2, ax3, ax4]:
		#		axis.legend()
		name_of_file = name_of_file+'_subplots'
		plt.savefig(name_of_file+'.png')
		plt.savefig(name_of_file+'.svg')

		# -------------------------------------------------------------------------
		# -------------------------------------------------------------------------
		# no of elements in positions in cluster, with maximum number of those positions.
		# given as percentage of number of atoms in cluster
		figure(figsize=(8, 3), dpi=80)
		plt.plot([0, self.greatest_no_of_atoms], [0, 100], c='k', ls='-', lw=2.0)

		plt.scatter(no_of_copper_atoms,np.array(max_vertex_data)*(100.0/float(self.greatest_no_of_atoms)),edgecolors='green', c='white', linewidths=2,label='max vertex')
		plt.scatter(no_of_copper_atoms,np.array(max_edge_data)*(100.0/float(self.greatest_no_of_atoms)),edgecolors='blue', c='white', linewidths=2,label='max edge')
		plt.scatter(no_of_copper_atoms,np.array(max_face_data)*(100.0/float(self.greatest_no_of_atoms)),edgecolors='red', c='white', linewidths=2,label='max face')
		plt.scatter(no_of_copper_atoms,np.array(max_bulk_data)*(100.0/float(self.greatest_no_of_atoms)),edgecolors=(255/255.0, 20/255.0, 147/255.0), c='white', linewidths=2,label='max bulk')

		plt.scatter(no_of_copper_atoms,np.array(vertex_data)*(100.0/float(self.greatest_no_of_atoms)),c='green',label='vertex')
		plt.scatter(no_of_copper_atoms,np.array(edge_data)*(100.0/float(self.greatest_no_of_atoms)),c='blue',label='edge')
		plt.scatter(no_of_copper_atoms,np.array(face_data)*(100.0/float(self.greatest_no_of_atoms)),c='red',label='face')
		plt.scatter(no_of_copper_atoms,np.array(bulk_data)*(100.0/float(self.greatest_no_of_atoms)),c=(255/255.0, 20/255.0, 147/255.0),label='bulk')

		plt.xlabel('$\mathregular{N_{'+str(self.focus_plot_with_respect_to_element)+'}}$')
		plt.ylabel('% '+str(self.focus_plot_with_respect_to_element)+' composition')
		plt.ylim((-0.5,100.5))
		plt.xlim((0-1,self.greatest_no_of_atoms+1))		
		plt.tight_layout()
		if self.add_legend:
			plt.legend()
		name_of_file = 'percent_'+str(self.focus_plot_with_respect_to_element)+'_comp_vs_no_'+str(self.focus_plot_with_respect_to_element)+'_atoms'
		plt.savefig(name_of_file+'.png')
		plt.savefig(name_of_file+'.svg')

		# --------------

		fig = figure(figsize=(8, 6), dpi=80)
		ax = fig.add_subplot(111)    # The big subplot
		ax1 = fig.add_subplot(221)
		ax2 = fig.add_subplot(222)
		ax3 = fig.add_subplot(223)
		ax4 = fig.add_subplot(224)

		# Turn off axis lines and ticks of the big subplot
		ax.spines['top'].set_color('none')
		ax.spines['bottom'].set_color('none')
		ax.spines['left'].set_color('none')
		ax.spines['right'].set_color('none')
		ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

		for axis in [ax1, ax2, ax3, ax4]:
			axis.plot([0, self.greatest_no_of_atoms], [0, 100], c='k', ls='-', lw=2.0,zorder=-10)
			axis.set_ylim((-0.5,100.5))
			axis.set_xlim((0-1,self.greatest_no_of_atoms+1))

		ax4.scatter(no_of_copper_atoms,np.array(max_vertex_data)*(100.0/float(self.greatest_no_of_atoms)),edgecolors='green', c='white', linewidths=2,label='max vertex')
		ax3.scatter(no_of_copper_atoms,np.array(max_edge_data)*(100.0/float(self.greatest_no_of_atoms)),edgecolors='blue', c='white', linewidths=2,label='max edge')
		ax2.scatter(no_of_copper_atoms,np.array(max_face_data)*(100.0/float(self.greatest_no_of_atoms)),edgecolors='red', c='white', linewidths=2,label='max face')
		ax1.scatter(no_of_copper_atoms,np.array(max_bulk_data)*(100.0/float(self.greatest_no_of_atoms)),edgecolors=(255/255.0, 20/255.0, 147/255.0), c='white', linewidths=2,label='max bulk')

		ax4.scatter(no_of_copper_atoms,np.array(vertex_data)*(100.0/float(self.greatest_no_of_atoms)),c='green',label='vertex')
		ax3.scatter(no_of_copper_atoms,np.array(edge_data)*(100.0/float(self.greatest_no_of_atoms)),c='blue',label='edge')
		ax2.scatter(no_of_copper_atoms,np.array(face_data)*(100.0/float(self.greatest_no_of_atoms)),c='red',label='face')
		ax1.scatter(no_of_copper_atoms,np.array(bulk_data)*(100.0/float(self.greatest_no_of_atoms)),c=(255/255.0, 20/255.0, 147/255.0),label='bulk')

		ax.set_xlabel('$\mathregular{N_{'+str(self.focus_plot_with_respect_to_element)+'}}$')
		ax.set_ylabel('Normalised % '+str(self.focus_plot_with_respect_to_element)+' composition')

		plt.tight_layout()
		#if self.add_legend:
		#	plt.legend()
		name_of_file = name_of_file+'_subplots'
		plt.savefig(name_of_file+'.png')
		plt.savefig(name_of_file+'.svg')

		# -------------------------------------------------------------------------
		return cluster_plot_data

	def record_to_excel(self, cluster_plot_data):
		cluster_plot_data = [(key, data) for key, data in cluster_plot_data.items()]
		cluster_plot_data.sort()

		workbook = Workbook()
		worksheet = workbook.active

		# pink, red, blue, green
		colours = {'bulk': 'FFC0CB', 'face': 'FF0000', 'edge': 'ADD8E6', 'vertex': '90EE90', 'None': 'FFFFFF'}
		def get_colour_name(name):
			for colour_name in colours.keys():
				if colour_name in name:
					return colour_name
			return 'None'

		naming = [str(tuple(self.elements))]+self.to_save
		for index in range(len(naming)):
			name = naming[index]
			worksheet.cell(column=index+1, row=1, value=str(name))
			worksheet.cell(column=index+1, row=1).fill = PatternFill("solid", fgColor=colours[get_colour_name(name)])

		for index in range(len(cluster_plot_data)):
			key, data = cluster_plot_data[index]
			worksheet.cell(column=1, row=index+2, value=str(key))
			for index2 in range(len(self.to_save)):
				name = self.to_save[index2]
				if 'percent' in name:
					number = round(data[name],1)
					if number < 0:
						number = ''
				else:
					number = data[name]
				worksheet.cell(column=index2+2, row=index+2, value=str(number))
				worksheet.cell(column=index2+2, row=index+2).fill = PatternFill("solid", fgColor=colours[get_colour_name(name)])
		# Save the file
		workbook.save("ClusterGeo_Data_"+str(self.focus_plot_with_respect_to_element)+".xlsx")
