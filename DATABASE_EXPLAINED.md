act_hi_actinst

ID_	varchar(64)	No
PROC_DEF_ID_	varchar(64)	No
PROC_INST_ID_	varchar(64)	No
EXECUTION_ID_	varchar(64)	No
ACT_ID_	varchar(255)	No
TASK_ID_	varchar(64)	Yes
CALL_PROC_INST_ID_	varchar(64)	Yes
ACT_NAME_	varchar(255)	Yes
ACT_TYPE_	varchar(255)	No
ASSIGNEE_	varchar(255)	Yes
START_TIME_	datetime	No
END_TIME_	datetime	Yes
DURATION_	bigint(20)	Yes
TENANT_ID_	varchar(255)	Yes


act_hi_detail

ID_	varchar(64)	No
TYPE_	varchar(255)	No
PROC_INST_ID_	varchar(64)	Yes
EXECUTION_ID_	varchar(64)	Yes
TASK_ID_	varchar(64)	Yes
ACT_INST_ID_	varchar(64)	Yes
NAME_	varchar(255)	No
VAR_TYPE_	varchar(255)	Yes
REV_	int(11)	Yes
TIME_	datetime	No
BYTEARRAY_ID_	varchar(64)	Yes
DOUBLE_	double	Yes
LONG_	bigint(20)	Yes
TEXT_	varchar(4000)	Yes
TEXT2_	varchar(4000)	Yes