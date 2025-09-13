try:
    file0= open("output.txt", "r")
    file0.close()

    input_text=str(input("Enter text towrite the file: "))
    with open("output.txt", 'w') as file1:
        writing= file1.write(input_text)
        print("Data successfully written to output.txt")

    add_text=str(input("Enter additional text to append: "))    
    with open("output.txt", "a") as file2:
        append=file2.write("\n" +add_text)
        print("Data successful added to output.txt")
        
    with open("output.txt" ,"r") as file2:
        print("Final conetnt of output.txt: ")
        read= file2.readline()
        print(read)
        read2= file2.readline()
        print(read2)        


except FileNotFoundError:
        print("File not FileNotFo")
