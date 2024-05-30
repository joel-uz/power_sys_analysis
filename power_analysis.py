import pypsa
import numpy as np

network = pypsa.Network()

buses_num = 3

network.add("Bus", "Bus 0", y=-30.5, x=25, v_nom=400, carrier="AC")
network.add("Bus", "Bus 1", y=-18.5, x=35.5, v_nom=400, carrier="AC")
network.add("Bus", "Bus 2", y=-18.5, x=35.5, v_nom=400, carrier="AC")

print(network.buses)

for i in range(buses_num):
    network.add(
        "Line",
        "Line No {}".format(i),
        bus0="Bus {}".format(i),
        bus1="Bus {}".format((i+1)%3),
        s_nom=500,
        x=1,
        r=1,
    )
print(network.lines)

network.add("Generator", "Gen 0", bus="Bus 0", p_set=0, control="Slack")
network.add("Generator", "Gen 1", bus="Bus 1", p_set=60, control="PQ")

print(network.generators)

network.add("Load", "New Load 0", bus="Bus 2", p_set=90, q_set=40)
print(network.loads)

val = network.pf()
print(val)

print("New lines -----------------")
print(network.lines_t.p0)
print(network.buses_t.v_ang * 180 / np.pi)
print(network.buses_t.v_mag_pu)



