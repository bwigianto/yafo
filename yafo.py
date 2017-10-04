import os
import argparse

def merge(x, y):
    z = x.copy()
    z.update(y)
    return z

def subfolders_loaded(dic):
    def subfolder(file):
        ext_to_folder = merge(dic, {
         'pdf': 'Documents',
         'docx': 'Documents',
         'doc': 'Documents',
         'epub': 'Documents',
    
         'png': 'Images',
         'jpeg': 'Images',
    
         'mp3': 'Music',
    
         'zip': 'Compressed',
         'tar': 'Compressed',
    
         'mp4': 'Movies',
         'mkv': 'Movies',
    
         'deb': 'Programs',
    
         'sh': 'Scripts'
        })
        ext = os.path.splitext(file)[0]
        if ext not in ext_to_folder:
            return 'Rest'
        return ext_to_folder[ext]
    return subfolder

def route(file, subfolder_mapper):
    dest = os.path.join(os.path.dirname(file), subfolder_mapper(file), os.path.basename(file))
    if not os.path.exists(os.path.dirname(dest)):
        os.mkdir(os.path.dirname(dest))
    os.rename(file, dest)
   
def discover(dir, subfolder_mapper):
    print('Current directory: ', dir)
    for folder, subfolders, filenames in os.walk(dir):
        if os.path.basename(folder) != os.path.basename(dir):
            continue
        for file in filenames:
            route(file, subfolder_mapper)

def main():
    parser = argparse.ArgumentParser(description='Organize files based on extension')
    parser.add_argument("--tex", help="organize .tex files",
                    action="store_true")
    args = parser.parse_args()
    subfolder_mapper = subfolders_loaded({}) if not args.tex else subfolders_loaded({'tex': 'TeX'})
    discover(os.getcwd(), subfolder_mapper)

main()
