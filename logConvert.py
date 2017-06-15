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
            var_map[(row["PROC_INST_ID_"], row["ACT_INST_ID_"])] = (row["NAME_"],row[type_map[row["VAR_TYPE_"]]])
except:
    print("Error: unable to fetch data")

print(var_map)

sql = "SELECT * FROM act_hi_actinst ORDER BY START_TIME_"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    n = 1
    inst_map = {}
    with open('/Users/YIZHONGQI/Desktop/log_convert.txt', 'a') as w:
        for row in results:
            proc_inst_id = row["PROC_INST_ID_"]

            if proc_inst_id not in inst_map:
                inner_order = 1
                inst_map[proc_inst_id] = 2
            else:
                inner_order = inst_map[proc_inst_id]
                inst_map[proc_inst_id] += 1

            towrite = str(n) + '\t' + proc_inst_id + '\t' + str(inner_order) + '\t' + row["ACT_ID_"]
            print(towrite)
            if (proc_inst_id, row['ID_']) in var_map:
                var = var_map[(proc_inst_id, row['ID_'])]
                towrite += '\t' + var[0] + "=" + str(var[1])

            towrite += '||||'

            for item in row.items():
                towrite += str(item) + ","
            towrite += '\n'
            w.write(towrite)

except Exception as e:
    print("Error: unable to fetch data", e)

db.close()