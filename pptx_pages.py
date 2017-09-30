import tempfile

def main():
    dirname=tempfile.mkdtemp(dir="./")
    print(dirname)

if __name__ == '__main__':
    main()