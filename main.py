from Fproc import Divide

def main():

    file_path = "var1.csv"
    processor = Divide(file_path)    
    ~processor     
    processor.split_dataset()
    processor.print_result()
if __name__ == "__main__":
    main()


