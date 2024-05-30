import pypsa
import numpy as np

""" This project focuses on building the power flow analysis using Newton Raphson 
Solution and with the help of PyPSA module the method is made a lot simpler.
"""


def check_connection_if_exist(n1, n2,origin_con, destn_con):
    for i in range(len(origin_con)):
        if (n1 == origin_con[i] and n2 == destn_con[i]) or (n2 == origin_con[i] and n1 == destn_con[i]):
            return True
    else:
        return False


def add_bus(network,number):
    network.add("Bus", f"Bus {number}", y=-30.5, x=25, v_nom=400, carrier="AC")


def add_line(network, number, bus1, bus2, res, react):
    network.add(
        "Line",
        "Line No {}".format(number),
        bus0="Bus {}".format(bus1),
        bus1="Bus {}".format(bus2),
        s_nom=500,
        x=react,
        r=res,
    )


# noinspection PyUnboundLocalVariable
def add_gen(network, number, connection, control, pset):

    if control == 1:
        cont = "Slack"
    elif control == 2:
        cont = "PQ"
    elif control == 3:
        cont = "PV"

    network.add("Generator", f"Gen {number}", bus=f"Bus {connection}", p_set=pset, control=cont)


def add_load(network, number, connection, pset, qset):
    network.add("Load", f"New Load {number}", bus=f"Bus {connection}", p_set=pset, q_set=qset)


# main
# define network
network = pypsa.Network()

# adding bus details
buses = int(input("Enter the number of buses: "))
for val in range(buses):
    add_bus(network, val)

print(f"\n Added {buses} buses to the network.")
print("Bus Details: \n")
print(network.buses)

# add the line details
print("Add the line details as follows:")

num = 0
origin = []
destn = []

while True:
    bus1 = int(input("Origin of line: "))
    bus2 = int(input("Ending of line: "))
    if bus2 >= buses or bus1 >= buses:
        print("No bus exist")
        continue
    if check_connection_if_exist(bus1, bus2, origin_con=origin, destn_con=destn):
        print("Connection already exist. Add a new connection!")
        continue

    origin.append(bus1)
    destn.append(bus2)
    res = float(input("Enter resistance of line: "))
    react = float(input("Enter reactance of line: "))

    add_line(network, number=num, bus1=bus1, bus2=bus2, res=res, react=react)
    num += 1
    print(origin)
    print(destn)

    if len(origin) == (buses*(buses-1)/2):
        print("Max connections reached!")
        break

    ask = input("Do you want new lines?[Y/n]: ")
    if ask.upper() != "Y":
        break

print("Finished connecting the lines.\n Line details are: ")
print(network.lines)

gen_load_num = 0
conn = []
controls = []

while True:
    connection = int(input("Enter the bus for connection: "))
    if connection in conn:
        print("Already connection is present!!")
        continue
    if connection >= buses:
        print("Bus doesnt exist!!")
        continue

    conn.append(connection)

    control = int(input("Enter the control method Slack[1], PQ[2] OR PV[3]: "))
    controls.append(control)

    p = float(input("Enter the active power: "))
    q = float(input("Enter the reactive power: "))
    ask = int(input("Do you want to add as Generators[1], loads[2] or none[0]: "))
    if ask == 1:
        add_gen(network, number=gen_load_num, connection=connection, control=control,
                pset=p)
        gen_load_num += 1
    elif ask == 2:
        add_load(network, number=gen_load_num, connection=connection,
                pset=p, qset=q)
        gen_load_num += 1
    elif ask == 0:
        if 1 not in controls:
            print("Add a slack bus! Add 1")
            continue
        else:
            k2 = input("Do you want to add more?[Y/n]: ")
            if k2.upper() != "Y":
                break
    if gen_load_num == buses:
        print("Max allocation!")
        break


print("Generator and load details: \n")
print(network.generators)
print(network.loads)

print("\n All parameters are taken in. Computing the newton raphson power flow.")
network.pf()

print("New values of angles are: ")
print(network.buses_t.v_ang * 180 / np.pi)
print("New values of voltage magnitudes are: ")
print(network.buses_t.v_mag_pu)







