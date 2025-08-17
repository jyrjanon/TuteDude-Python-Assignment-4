def read_file():
    filename="sample.txt"
    try:
        with open(filename,"r") as file:
            print("Reading File Cntents:")
            for i,line in enumerate(file,start=1):
                print(f"Line {i}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


read_file()

