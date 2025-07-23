target = "xilinx"
action = "synthesis"

syn_device = "xc7a200t"
syn_grade = "-2"
syn_package = "ffg1156"
syn_top = "merge_inst_tb"
syn_project = "merge_inst_tb"
syn_tool = "vivado"

files = [ "../files/gate2_param.v", "../files/merge_inst_tb.sv" ]
