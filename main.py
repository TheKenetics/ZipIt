import os, shutil, sys

"""
Zip It
Python script for finding folders in a directory, and zipping each of those folders into its own zip file.

Usage:
	python3 main.py C:/Path/to/folder/

	If given a path to a folder, it will zip each folder in that directory.
	Otherwise, it will zip each folder in the current working directory.
"""

def get_folder_list(folder):
	# Returns list of folders in folder
	return [item for item in os.listdir(folder) if os.path.isdir( os.path.join(folder, item) )]

def main():
	current_folder = None
	if len( sys.argv ) > 1:
		current_folder = sys.argv[1]
	else:
		current_folder = os.getcwd()
	
	print("Current Folder = " + current_folder)

	folders = get_folder_list(current_folder)
	
	for folder in folders:
		print( "Zipping {0} into {0}.zip".format(folder) )
		shutil.make_archive(folder, 'zip', folder)

if __name__ == "__main__":
	main()