def main():
    filename = input("Enter a file name: ")

    infile = open(filename, "r")

    contents = infile.read()

    for i in range(1, 6):

        print(contents)

    infile.close()

main()