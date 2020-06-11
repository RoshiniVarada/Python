def string_alternative(inputString):
    print("Output String: {}".format(inputString[::2]))

def main():
    inputString=input("Enter the Input String:")
    string_alternative("".join(inputString.split()))

if __name__=="__main__":
    main()
