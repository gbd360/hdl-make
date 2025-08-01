target = "xilinx"
action = "synthesis"

syn_device = "xc7a200t"
syn_grade = "-2"
syn_package = "ffg1156"
syn_top = "wrong_vlog_parser"
syn_project = "wrong_vlog_parser"
syn_tool = "vivado"

files = [ 
    "wrong_vlog_parser.sv",
    "asser.sv",
    "dumb_function_on.sv",
    "dumb_function_tw.sv",
    "foreac.sv",
]
