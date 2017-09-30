import tempfile
import zipfile
import os
import sys
import shutil
import re

def main():
    args=sys.argv
    if len(args) < 2:
        print("please input pptx file..")
        sys.exit(1)
    
    regex_pattern=re.compile(r".+\.pptx$")
    for arg in args[1:]:
        if regex_pattern.match(arg):    
            dir_path=tempfile.mkdtemp(dir="./")
            pptx_file=os.path.join(arg)
            
            with zipfile.ZipFile(pptx_file,"r") as z_file:
                z_file.extractall(path=dir_path)

            slides_path=os.path.join(dir_path,"ppt","slides")
            slides_xmls=[i for i in os.listdir(slides_path) if os.path.isfile(os.path.join(slides_path,i))]
            
            print(arg+", "+str(len(slides_xmls))+" pages")

            shutil.rmtree(dir_path)
        else:
            print(arg+" is not pptx file")

if __name__ == '__main__':
    main()