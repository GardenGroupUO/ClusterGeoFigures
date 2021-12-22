# ClusterGeoFigures: Obtaining Plots about Geometric Properties of Nanoclusters and Other Chemical Systems

[![PyPI - Python Version](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://docs.python.org/3/)
[![Citation](https://img.shields.io/badge/Citation-click%20here-green.svg)](https://dx.doi.org/10.1021/acs.jcim.0c01128)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/GardenGroupUO/ClusterGeoFigures)](https://github.com/GardenGroupUO/ClusterGeoFigures)
[![Licence](https://img.shields.io/github/license/GardenGroupUO/ClusterGeoFigures)](https://www.gnu.org/licenses/agpl-3.0.en.html)
[![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/GardenGroupUO/ClusterGeoFigures)](https://lgtm.com/projects/g/GardenGroupUO/ClusterGeoFigures/context:python)

Authors: Geoffrey R. Weal, Caitlin A. Casey-Stevens and Dr. Anna L. Garden (University of Otago, Dunedin, New Zealand)

Group page: https://blogs.otago.ac.nz/annagarden/

Page to cite with work from: *XXX*; XXX; 

## What is this Program?



## Pre-Requisite Programs

ClusterGeoFigures requires the following programs before it can be used:

* Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/
* ASAP3: https://wiki.fysik.dtu.dk/asap
* Packaging
* Openpyxl

The easiest way to install these is through pip. Type the following two lines into the terminal: 

.. code-block:: bash

	pip3 install --upgrade --user ase packaging
	pip3 install --upgrade --user asap3==3.11.10
	pip3 install --upgrade --user openpyxl

See https://pip.pypa.io/en/stable/installation/ if you do not have pip installed on your computer. 

## Installation

To install this program on your computer, pop open your terminal, ``cd`` to where you want to place this program on your computer, and clone the program to your computer by typing the following into your terminal:

```
git clone https://github.com/GardenGroupUO/ClusterGeoFigures
```

If you do not have ``git`` installed on your computer, see https://www.atlassian.com/git/tutorials/install-git

Once you have done this, type ``pwd`` into the terminal and copy this path into your ``~\.bashrc`` in the following format:

```bash
#####################################################################################
# These lines will allow python to locate this program on your computer.
export PATH_TO_ClusterGeoFigures='/PATH_GIVEN_BY_THE_PWD_COMMAND/ClusterGeoFigures'
export PYTHONPATH="$PATH_TO_ClusterGeoFigures":$PYTHONPATH
#####################################################################################
```

This will allow your computer to run this program through your terminal on python3.

## How to Run ClusterGeoFigures

An example of the script used to run this program is given below, called ``Run_ClusterGeoFigures.py``.

```python
from ClusterGeoFigures import ClusterGeoFigures_Program

r_cut = 2.9
elements = ['Cu','Pd']
focus_plot_with_respect_to_element = 'Pd'
path_to_xyz_files = 'dft_mins'
add_legend = False

ClusterGeoFigures_Program(r_cut,elements,focus_plot_with_respect_to_element,path_to_xyz_files,add_legend)
```

When you execute this program by running ``python3 Run_ClusterGeoFigures.py`` in the terminal, ClusterGeoFigures will 

## What will ClusterGeoFigures do when you run the ``Run_ClusterGeoFigures.py`` script?



## Output files that are created by ClusterGeoFigures

Figures placed in folder called ``ClusterGeoFigures_figures_folder``

## Other useful programs in ClusterGeoFigures



## About

<div align="center">

| Python        | [![PyPI - Python Version](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://docs.python.org/3/) | 
|:-------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Repositories  | [![GitHub release (latest by date)](https://img.shields.io/github/v/release/GardenGroupUO/ClusterGeoFigures)](https://github.com/GardenGroupUO/ClusterGeoFigures) |
| Documentation | [![GitHub release (latest by date)](https://img.shields.io/github/v/release/GardenGroupUO/ClusterGeoFigures)](https://github.com/GardenGroupUO/ClusterGeoFigures) | 
| Citation      | [![Citation](https://img.shields.io/badge/Citation-click%20here-green.svg)](https://dx.doi.org/10.1021/acs.jcim.0c01128) | 
| Tests         | [![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/GardenGroupUO/ClusterGeoFigures)](https://lgtm.com/projects/g/GardenGroupUO/ClusterGeoFigures/context:python)
| License       | [![Licence](https://img.shields.io/github/license/GardenGroupUO/ClusterGeoFigures)](https://www.gnu.org/licenses/agpl-3.0.en.html) |
| Authors       | Geoffrey R. Weal, Caitlin A. Casey-Stevens, and Dr. Anna L. Garden |
| Group Website | https://blogs.otago.ac.nz/annagarden/ |

</div>
