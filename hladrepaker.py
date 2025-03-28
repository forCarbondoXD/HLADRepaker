import os
from PIL import Image
import zipfile
import sys
from pathlib import Path

def dbr_fix(a):
    return a.replace('\\', '/')

def has_args(args):
    CURRENT_WORK = args[1]
    if os.path.isdir(CURRENT_WORK):
        print("is folder, onto folder processor")
        folder_process(CURRENT_WORK)
    else:
        print("not a folder, onto zip processor")
        zip_process(CURRENT_WORK)
    
def folder_process(CURRENT_WORK):
    print(f"folder_process working in {CURRENT_WORK}")
    newfolder = newfolder_processor(CURRENT_WORK)
    print(newfolder)
    CURRENT_DIR = os.listdir(CURRENT_WORK)   
    for i in CURRENT_DIR:
        this_file = f"{CURRENT_WORK}/{i}"
        if Path(this_file).suffix == ".webp":
            image_processor(this_file, newfolder)
    
def newfolder_processor(dir):
    fold_replace = dir.replace('\\', '/')
    if fold_replace.endswith('/'): fold_replace = fold_replace[:-1]
    folder_extract = fold_replace.split("/")
    folder_name = folder_extract[-1]
    folder_path = dir.replace(folder_name, '') # Without Contains a File Name Here.
    folder_info = f"""{folder_path}/[HLADRPK] {folder_name}"""
    os.mkdir(folder_info)
    return folder_info
    
def zip_process(zip_f):
    zip_f = dbr_fix(zip_f)
    splited = zip_f.split("/")
    zip_name = splited[-1]
    zip_path = zip_f.replace(zip_name, '')
    
    tmp = f'{zip_path}/{zip_name.replace(".zip", "")}'
    
    if not os.path.exists(tmp):
        os.mkdir(tmp)
    else:
        os.rmdir(tmp)
        os.mkdir(tmp)
        

    with zipfile.ZipFile(zip_f, 'r') as zip_ref:
        zip_ref.extractall(f'{tmp}')
    
    folder_process(tmp)

    
def image_processor(imgin, output):
    imgin = dbr_fix(imgin)
    output = dbr_fix(output)
    
    imgin_cut = imgin.split('/')[-1]
    
    print(f"""processing with {output}/{imgin.replace('.webp', '.png')}""")
    IMG_EXPORT_DEF = ".png"
    img = Image.open(imgin);
    img.load()
    img.save(f"""{output}/{imgin_cut.replace('.webp', '.png')}""")
    print("image_processor, ok!")
    

if __name__ == "__main__":
    has_args(sys.argv)
    
    print("WORK OVER")
    # input()