from ClusterGeoFigures import ClusterGeoFigures_Program

r_cut = 2.9
elements = ['Cu','Pd']
focus_plot_with_respect_to_element = 'Pd'
path_to_xyz_files = 'dft_mins'
add_legend = False

ClusterGeoFigures_Program(r_cut,elements,focus_plot_with_respect_to_element,path_to_xyz_files,add_legend)
