# This is a script with constraints that mustn't be run during
# project build, just added to constr_1 list.
foreach inst [get_cells -hier -filter {(ORIG_REF_NAME == top || REF_NAME == top)}] {
    # reset synchronization
    set async_counter [get_cells -quiet -hier -regexp ".*/cnt\\\[\\d+\\\]" -filter "PARENT == $inst"]

    set_property ASYNC_REG TRUE $async_counter
    set_false_path -to [get_pins -of_objects $async_counter -filter {IS_PRESET || IS_RESET}]
}
