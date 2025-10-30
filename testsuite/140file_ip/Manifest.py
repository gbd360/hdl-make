action = "synthesis"
language = "vhdl"

syn_device = "xc7z030"
syn_grade = "-2"
syn_package = "ffg676"

syn_top = "gate3"
syn_project = "gate.xise"

syn_tool = "vivado"

#files = [ "../files/gate3.vhd", FileIP("my_ip.tcl", "gate") ]
files = [ "../files/gate3.vhd", ("my_ip.tcl", "gate") ]
