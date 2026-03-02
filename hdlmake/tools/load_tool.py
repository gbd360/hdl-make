"""Registry module for the tools"""


import logging
import importlib


module_registry = {
    # format: (tool_name, type): (module_name, class_name)
    ('ise', 'syn'): ('.ise', 'ToolISE'),
    ('planahead', 'syn'): ('.planahead', 'ToolPlanAhead'),
    ('quartus', 'syn'): ('.quartus', 'ToolQuartus'),
    ('diamond', 'syn'): ('.diamond', 'ToolDiamond'),
    ('ghdl', 'syn'): ('.ghdl_syn', 'GhdlSyn'),
    ('libero', 'syn'): ('.libero', 'ToolLibero'),
    ('liberosoc', 'syn'): ('.liberosoc', 'ToolLiberoSoC'),
    ('icestorm', 'syn'): ('.icestorm', 'ToolIcestorm'),
    ('vivado', 'syn'): ('.vivado', 'ToolVivado'),
    ('vivado_sim', 'sim'): ('.vivado_sim', 'ToolVivadoSim'),
    ('iverilog', 'sim'): ('.iverilog', 'ToolIVerilog'),
    ('isim', 'sim'): ('.isim', 'ToolISim'),
    ('modelsim', 'sim'): ('.modelsim', 'ToolModelsim'),
    ('active_hdl', 'sim'): ('.active_hdl', 'ToolActiveHDL'),
    ('riviera', 'sim'): ('.riviera', 'ToolRiviera'),
    ('ghdl', 'sim'): ('.ghdl', 'ToolGHDL'),
    ('nvc', 'sim'): ('.nvc', 'ToolNVC'),
    ('gowin', 'syn'): ('.gowin', 'ToolGowin'),
    ('vunit', 'sim'): ('.vunit', 'ToolVunitSim'),
}

custom_module_registry = {}

def register_tool(identifier, class_):
    """Register a tool"""
    custom_module_registry[identifier] = class_


def load_tool(tool_name, filter_type):
    '''Function that loads a tool and initializes it'''
    # load builtin modules
    try:
        module_name, class_name = module_registry[(tool_name, filter_type)]
    except KeyError:
        pass
    else:
        module = importlib.import_module(module_name, package='hdlmake.tools')
        class_ = getattr(module, class_name, None)
        if class_ is None:
            raise ModuleNotFoundError(f'Class {class_name} not found in module {module_name}')
        logging.debug(f'Loading module: {tool_name!r}')
        return class_

    # try custom modules
    try:
        class_ = custom_module_registry[tool_name]
    except KeyError as error:
        raise Exception(f'Tool {tool_name!r} not known') from error
    else:
        logging.debug(f'Loading custom module: {tool_name!r}')
        return class_


def load_syn_tool(tool_name):
    """Function that checks the provided module_pool and generate an
    initialized instance of the appropriate synthesis tool"""
    class_ = load_tool(tool_name, 'syn')
    return class_()


def load_sim_tool(tool_name):
    """Function that checks the provided module_pool and generate an
    initialized instance of the appropriate simulation tool"""
    class_ = load_tool(tool_name, 'sim')
    return class_()
