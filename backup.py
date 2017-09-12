from distutils.dir_util import copy_tree
import os

if not os.path.exists('/media/fronchetti/3E1BCE024D60D3AF/TCC-Backup'):
	os.makedirs('/media/fronchetti/3E1BCE024D60D3AF/TCC-Backup')

copy_tree('Dataset','/media/fronchetti/3E1BCE024D60D3AF/TCC-Backup')
