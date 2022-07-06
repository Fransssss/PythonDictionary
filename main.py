# dictionary = a changeable , unordered collection of unique key:value pairs

nation_capital = {"Argentina" : "Buenos Aires", "Belgium" : "Brussels", "Canada" : "Ottawa"
    , "Denmark" : "Copenhagen", "France" : "Paris", "USA" : "Washington DC"}

print("\n == Nation and its Capital Database == ")
print("1. List of all Nation and its Capital")
print("2. List of Nation")
print("3. List of Capital")
print("4. Add a Nation and its Capital")
print("5. Remove a Nation and its Capital")
print("6. Clear all Nation and its Capital")
print("E. Exit")
choice = input("choice: ")

while choice != 'E' and choice !='e':
    if choice == '1':
        print("\n[List of all Nation and its Capital]")
        print(nation_capital)
    elif choice == '2':
        print("\n[List of Nation]")
        print(nation_capital.keys())
    elif choice == '3':
        print("\n[List of Capital]")
        print(nation_capital.values())
    elif choice == '4':
        print("\n[Add a Nation and its Capital]")
        nat = input("name of a nation: ")
        capt = input("name of the capital: ")
        if len(nat) == 0 or len(capt) == 0:
            print("[Input incomplete]")
        else:
            nation_capital.update({nat : capt})
            print("new item added")
    elif choice == '5':
        print("\n[Remove a Nation and its Capital]")
        nat = input("name the nation to remove: ")
        if len(nat) == 0:
            print("[No input]")
        else:
            nation_capital.pop(nat)
            print("item removed")
    elif choice == '6':
        ar_u_sure = input("\nare you sure (Y/N)? ")
        if ar_u_sure == 'Y' or ar_u_sure == 'y':
            nation_capital.clear()
            print("item cleared")
        elif ar_u_sure == 'N' or ar_u_sure == 'n':
            print("command cancelled")
        else:
            print("input should be 'Y' or 'N'")
    else:
        print("\n[Invalid input]")

    print("\n == Nation and its Capital Database == ")
    print("1. List of all Nation and its Capital")
    print("2. List of Nation")
    print("3. List of Capital")
    print("4. Add a Nation and its Capital")
    print("5. Remove a Nation and its Capital")
    print("6. Clear all Nation and its Capital")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\nExit Program")

#print(nation_capital.values()) # capitals only
#print(nation_capital.keys())   # nations only
#print(nation_capital.items()) # nation and capital