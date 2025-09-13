try:
    
    with open("sample.txt", "r")as file1:
        print("Reading file content....")
        contents= file1.readline()
        print("Line 1: " + contents)
        contents1= file1.readline()
        print("Line 2: " + contents1)
    
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
