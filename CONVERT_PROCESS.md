Need 2 tables from act_hi:
    act_hi_actinst
    act_hi_detail
    
    
act_hi_detail:
    keeps every change of each variable
    
    read the table, and keep a map: (proc_inst_id, act_inst_id): (var, var_value)
    
act_hi_actinst:
    contains all other info for the new format need
    