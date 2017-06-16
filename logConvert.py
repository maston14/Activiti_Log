import pymysql

type_map = {"long":"LONG_", "double":"DOUBLE_", "string":"TEXT_"}

db = pymysql.connect("localhost","root","123456","activiti" )

cursor = db.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM act_hi_detail"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    var_map = {}
    for row in results:
        if row["ACT_INST_ID_"] != None:
            if (row["PROC_INST_ID_"], row["ACT_INST_ID_"]) not in var_map:
                var_map[(row["PROC_INST_ID_"], row["ACT_INST_ID_"])] = []
            # use a list because a act_inst can have multiple variables
            var_map[(row["PROC_INST_ID_"], row["ACT_INST_ID_"])].append((row["NAME_"],row[type_map[row["VAR_TYPE_"]]]))
except:
    print("Error: unable to fetch data")

print(var_map)

sql = "SELECT * FROM act_hi_actinst ORDER BY START_TIME_"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    n = 1
    # for inner order
    inst_map = {}
    # for global var
    inst_var_map = {}

    with open('/Users/YIZHONGQI/Desktop/log_convert.txt', 'a') as w:
        for row in results:
            proc_inst_id = row["PROC_INST_ID_"]

            if proc_inst_id not in inst_map:
                inner_order = 1
                inst_map[proc_inst_id] = 2
            else:
                inner_order = inst_map[proc_inst_id]
                inst_map[proc_inst_id] += 1

            common_to_write = str(n) + '|' + proc_inst_id + '|' + str(inner_order) + '|' + row["ACT_ID_"] + '|'
            print(common_to_write)
            start_towrite = common_to_write + "in:"
            end_towrite = common_to_write + 'out:'

            # get the variable that already exists
            if proc_inst_id not in inst_var_map:
                inst_var_map[proc_inst_id] = {}
            for k, v in inst_var_map[proc_inst_id].items():
                start_towrite += k + '=' + str(v) + ','

            # update new variable
            if (proc_inst_id, row['ID_']) in var_map:
                var_list = var_map[(proc_inst_id, row['ID_'])]

                for var in var_list:
                    inst_var_map[proc_inst_id][var[0]] = var[1]
                    end_towrite += var[0] + "=" + str(var[1]) + ','


            start_towrite += '\n'
            end_towrite += '\n'

            w.write(start_towrite)
            w.write(end_towrite)

except Exception as e:
    print("Error: unable to fetch data", e)

db.close()