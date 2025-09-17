target = "xilinx"
action = "synthesis"
language = "verilog"

syn_device = "xc7a200t"
syn_grade = "-2"
syn_package = "ffg1156"
syn_top = "constr_test"
syn_project = "constr_test"
syn_tool = "vivado"

files = ["constr_test.sv"]

constraints = [
    "constr.xdc",
    "constr.tcl",
]

modules = {
    "local" : "constr_module",
}