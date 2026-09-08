action = "simulation"

sim_tool="nvc"
nvc_opt="--std=2008"

top_module = "gate8"

modules = {
    'local': [
        'gatelib_src',
    ],
}

files = [ "../files/gate8.vhdl" ]
