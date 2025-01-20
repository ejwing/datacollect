#from util import download_all_realestate



# unzip everything in download folder
import os, zipfile, pandas

def unzip_all(fromfolder:str = ".", tofolder:str = "."):
    fromfolder = os.path.abspath(fromfolder)
    tofolder = os.path.abspath(tofolder)
    for name in os.listdir(fromfolder):
        fullname = os.path.join(fromfolder, name)
        if os.path.isfile(fullname) and zipfile.is_zipfile(fullname):
            base, extension = os.path.splitext(name)
            dstfolder = os.path.join(tofolder, base)
            print(f"zipfile: '{fullname}' unzip to: '{dstfolder}'")
            with zipfile.ZipFile(fullname) as zf:
                zf.extractall(dstfolder)
        else:
            print(f"others: '{fullname}'")


def read_schema(folder:str=".", schema:str="schema-main.csv"):
    filepath = os.path.abspath(folder)
    filepath = os.path.join(filepath, schema)
    if os.path.isfile(filepath):
        df = pandas.read_csv(filepath)
        for a, b in df.items():
            print(a)
            print()
            print(b)
            print()
    else:
        print(f"can't find the file. {filepath}")

def walk_dir(dir="."):
    curr_path = os.path.abspath(dir)
    print("path : {path}".format(path=curr_path))
    for name in os.listdir(curr_path):
        if os.path.isfile(name):
            print(f"file: '{name}'")
        elif os.path.isdir(name):
            print(f"folder: '{name}'")
        else:
            print(f"???: '{name}'")
        print("full path: {path}".format(path=os.path.join(curr_path, name)))