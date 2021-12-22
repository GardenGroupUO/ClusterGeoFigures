



# -----------------------------------------------------------------------------------------

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