def main():
    arr = input("Please provide a list of numbers, separated by a space:\n").split(" ")
    ints = []
    for str in arr:
        ints.append(int(str))
    arr = ints
    action = input("Asc, Desc or None:\n")
    
    if action.lower() == "asc":
        print(sorted(arr))
    elif action.lower() == "desc":
        print(sorted(arr, reverse=True))
    else:
        print(arr)
    

if __name__ == "__main__":
    main()