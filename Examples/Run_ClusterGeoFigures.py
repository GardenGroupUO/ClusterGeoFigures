from ClusterGeoFigures import ClusterGeoFigures_Program

r_cut = 2.9
elements = ['Cu','Pd']
focus_plot_with_respect_to_element = 'Pd'
path_to_xyz_files = 'dft_mins'
add_legend = False

bulk_colour = (251/255.0,180/255.0,185/255.0) #'#FFFFFF'
face_colour = (247/255.0,104/255.0,161/255.0) #'#FF0000'
vertex_colour = (197/255.0,27/255.0,138/255.0) #'#90EE90'
edge_colour = (122/255.0,1/255.0,119/255.0) #'#ADD8E6'
none_colour = '#FFFFFF'

ClusterGeoFigures_Program(r_cut,elements=elements,focus_plot_with_respect_to_element=focus_plot_with_respect_to_element,path_to_xyz_files=path_to_xyz_files,add_legend=add_legend,bulk_colour=bulk_colour,face_colour=face_colour,vertex_colour=vertex_colour,edge_colour=edge_colour,none_colour=none_colour)
