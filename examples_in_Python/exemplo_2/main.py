import find_nemo

def menu():
    print("=-" * 18)
    print("=-" * 5 + " FIND NEMO " + "=-" * 5)
    print("=-" * 18)

    text = str(input("Write where to look for Nemo: "))
    result = find_nemo.nemo(text)

    print(result)

if(__name__ == "__main__"):
    menu()
    