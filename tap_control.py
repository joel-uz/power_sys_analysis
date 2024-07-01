import pandapower.networks as nw
import pandapower.control as cn
import pandapower as pp

net = nw.mv_oberrhein()
cn.DiscreteTapControl(net, 114,  0.96, 1.01)
print(net.trafo.tap_pos)

pp.runpp(net, run_control = True)
print(net.trafo.tap_pos)
print(net.res_bus.loc[net.trafo.lv_bus, "vm_pu"])