"""The code is for calculation of y bus for a matrix given."""


def number_check(x,y,lst):
    for value in lst:
        if (value[0] == x and value[1] == y) or (value[0] == y and value[1] == x):
            return True

    return False


def y_bus():

    bus = int(input("Enter the number of buses: "))
    print('\n')
    # for assigning size of the square matrix

    number_of_connections = bus*(bus-1)/2

    print("For adding in the parameters go in the i, j, R, X values format")
    connections = []
    check = 'Y'

    while check == "Y":
        current = input("Enter the params in [i,j,R,X] format: ").split(",")
        if current[0] == current[1] or number_check(current[0],current[1],connections):
            print("Redundancy of data. Try again!!")
            continue

        connections.append(current)
        print(connections)
        print("added these number to the list so far \n")

        if len(connections) == number_of_connections:
            print("Max. connections reached")
            break

        check = input("You want to continue adding?[Y/n]: ").upper()
        if check != "Y":
            print("Error in connection.. Add the missing bus details")
            check = "Y"


    print(connections)
    print('\n')
    # assigning the equivalent impedance value to the bus connection

    main_dict = {}

    for every in connections:
        main_dict[str(every[0] + every[1])] = complex(float(every[2]), float(every[3]))

    print("finished connecting")
    print(main_dict)

    # completing the matrix
    matrix = []

    for i in range(0, bus):
        new_set = []
        for j in range(0, bus):
            if i == j:
                sum = 0
                for every in connections:
                    if int(every[0]) == i + 1 or int(every[1]) == i + 1:
                        sum += 1 / complex(float(every[2]), float(every[3]))
                new_set.append(sum)
            else:  # i=0 j=1
                value = 0
                for every in connections:
                    if int(every[0]) == (j + 1) and int(every[1]) == (i + 1):
                        value = -1 / complex(float(every[2]), float(every[3]))

                    elif int(every[1]) == (j + 1) and int(every[0]) == (i + 1):
                        value = -1 / complex(float(every[2]), float(every[3]))

                new_set.append(value)

        matrix.append(new_set)
    print("The resultant Y bus matrix is: \n")
    print(matrix)
    return matrix, bus