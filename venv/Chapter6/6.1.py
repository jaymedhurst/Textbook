def main():
    my_file = open("number.txt","r")

    file_contents = my_file.read()

    my_file.close()

    print(file_contents)

main()