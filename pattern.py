for x in range(1, 6):
    for y in range(1, 6):
        if x==1 or y==1 or x==5 or y==5:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()