import pandapower as pp
import pandapower.networks as np
import pandas as pd

# create an empty network
grid = pp.create_empty_network()

# To add to the empty network, we will use an excel sheet storing the details
new = pd.read_excel("grid_data.xlsx", sheet_name="bus", index_col=0)
for each in new.index:
    pp.create_bus(grid, vn_kv=new.at[each, "voltage"])

new = pd.read_excel("grid_data.xlsx", sheet_name="load", index_col=0)
for each in new.index:
    pp.create_load(grid, bus=new.at[each,"bus"], p_mw=new.at[each, "p"])

new = pd.read_excel("grid_data.xlsx", sheet_name="ext_grid", index_col=0)
for each in new.index:
    pp.create_ext_grid(grid, bus=new.at[each,"bus"], vm_pu=new.at[each,"vm_pu"], va_degree=new.at[each,"va_degree"])

new = pd.read_excel("grid_data.xlsx", sheet_name="line", index_col=0)
for each in new.index:
    pp.create_line_from_parameters(grid, *new.loc[each, :])


new = pd.read_excel("grid_data.xlsx", sheet_name="gen", index_col=0)
for each in new.index:
    pp.create_sgen(grid, name=new.at[each, "name"],bus=new.at[each, "bus"], p_mw=new.at[each, "p_mw"],
                  max_q_mvar=new.at[each, "q_mvar"], scaling=new.at[each, "scaling"],
                  sn_mva=new.at[each, "sn_mva"], type=new.at[each, "type"])

new = pd.read_excel("grid_data.xlsx", sheet_name="transfo", index_col=0)
for each in new.index:
    pp.create_transformer(grid, hv_bus=new.at[each,"hv"], lv_bus=new.at[each,"lv"],
                          std_type=new.at[each,"std"])

# Grid is formed and the following details are printed
print(grid)

pp.runpp(grid)
# print out the results after power flow analysis of the grid
print(grid.res_bus)
print(grid.res_line)