import tempfile
import zipfile
import os
import sys
import shutil

def main():
    args=sys.argv
    dir_path=tempfile.mkdtemp(dir="./")
    pptx_file=os.path.join(args[1])
    
    with zipfile.ZipFile(pptx_file,"r") as z_file:
        z_file.extractall(path=dir_path)

    slides_path=os.path.join(dir_path,"ppt","slides")
    slides_xmls=[i for i in os.listdir(slides_path) if os.path.isfile(os.path.join(slides_path,i))]
    
    print(len(slides_xmls))

    shutil.rmtree(dir_path)

if __name__ == '__main__':
    main()