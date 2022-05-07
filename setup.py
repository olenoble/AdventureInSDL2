# script to automate the EXE creation
import os
from distutils.dir_util import copy_tree
import shutil

# need to generate the .gitignore

if __name__ == '__main__':
    game_name = 'scandyum'
    folders_to_copy = ['assets']
    # file_to_compile = 'main'
    file_to_compile = 'main'

    # compile_options = ['-w', '--onefile', '--icon=scandyum.ico']
    compile_options = ['-w', '--onedir', '--icon=scandyum.ico']

    full_recompile = True

    # if full_recompile, remove compilation folders
    if full_recompile:
        try:
            shutil.rmtree('./dist')
            shutil.rmtree('./build')
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

    # now compile
    shell_cmd = ' '.join(['pyinstaller'] + compile_options + [file_to_compile + '.py'])
    os.system(shell_cmd)

    # copy over assets
    is_onedir = '--onedir' in compile_options
    for folder in folders_to_copy:
        tofolder = './dist/' + ((file_to_compile + '/') if is_onedir else '')  + folder
        copy_tree(folder, tofolder)

    # rename file
    dest_folder = './dist/' + ((file_to_compile + '/') if is_onedir else '')
    os.rename(dest_folder + file_to_compile + '.exe', dest_folder + game_name + '.exe')

    # create gitignore file
    with open('./build/.gitignore', 'wb') as file:
        file.write(b'\n*\n')

    with open('./dist/.gitignore', 'wb') as file:
        file.write(b'\n*\n')
