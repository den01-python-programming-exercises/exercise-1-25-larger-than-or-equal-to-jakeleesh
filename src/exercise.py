def main():
    #write your code below this line
    first = int(input("Give the first number:"))
    second = int(input("Give the second number:"))
    if (first > second):
        print("Greater number is: " + str(first))
    elif (second > first):
        print("Greater number is: " + str(second))
    elif (first == second):
        print("The numbers are equal!")

if __name__ == '__main__':
    main()
