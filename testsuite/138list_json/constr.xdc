# This is a regular file with constraints that
# must be just added to constr_1 list
create_clock -add -name sys_clk_pin -period 8.00 -waveform {0 4} [get_ports i_clk]
