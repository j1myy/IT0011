def show_menulol():
    print("==== Menu ====")
    print("1. Part A")
    print("2. Part B")
    print("3. Exit")
    print("=================")

def option1():
    print("Part A:")
    for q in range(1, 6):

        for w in range(1, 6 - q):
            print(" ", end="")


        for k in range(1, q + 1):
            print(k, end="")

        print()

def option2():
    print("Part B:")

    v = 1
    while v <= 5:

        b = 1
        while b <= v:
            print(v, end="")
            b += 1
        print()
        v += 1

def main():
    while True:
        show_menulol()
        choice = input(" select an option (1-3):")

        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            print("Exiting... byeee byeee")
            break
        else:
            print("Invalid option lol ;]")

if __name__ == "__main__":
    main()
