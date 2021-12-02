#-------------------------------------------------------------------------------
# Name:    fbconstants
# Purpose:   constants used by fbclient
#
# Author:   Boris
#
# Created:   27.02.2012
# Copyright:  (c) Boris 2012
# Licence:   <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from ctypes import c_byte


##firebird_dll = 'fbclient.dll'
firebird_dll = 'libfbclient.so'

##
## Database parameter block constants
##
isc_dpb_version1        = c_byte(1)
isc_dpb_cdd_pathname      = c_byte(1)
isc_dpb_allocation       = c_byte(2)
isc_dpb_journal        = c_byte(3)
isc_dpb_page_size       = c_byte(4)
isc_dpb_num_buffers      = c_byte(5)
isc_dpb_buffer_length     = c_byte(6)
isc_dpb_debug         = c_byte(7)
isc_dpb_garbage_collect    = c_byte(8)
isc_dpb_verify         = c_byte(9)
isc_dpb_sweep         = c_byte(10)
isc_dpb_enable_journal     = c_byte(11)
isc_dpb_disable_journal    = c_byte(12)
isc_dpb_dbkey_scope      = c_byte(13)
isc_dpb_number_of_users    = c_byte(14)
isc_dpb_trace         = c_byte(15)
isc_dpb_no_garbage_collect   = c_byte(16)
isc_dpb_damaged        = c_byte(17)
isc_dpb_license        = c_byte(18)
isc_dpb_sys_user_name     = c_byte(19)
isc_dpb_encrypt_key      = c_byte(20)
isc_dpb_activate_shadow    = c_byte(21)
isc_dpb_sweep_interval     = c_byte(22)
isc_dpb_delete_shadow     = c_byte(23)
isc_dpb_force_write      = c_byte(24)
isc_dpb_begin_log       = c_byte(25)
isc_dpb_quit_log        = c_byte(26)
isc_dpb_no_reserve       = c_byte(27)
isc_dpb_user_name       = c_byte(28)
isc_dpb_password        = c_byte(29)
isc_dpb_password_enc      = c_byte(30)
isc_dpb_sys_user_name_enc   = c_byte(31)
isc_dpb_interp         = c_byte(32)
isc_dpb_online_dump      = c_byte(33)
isc_dpb_old_file_size     = c_byte(34)
isc_dpb_old_num_files     = c_byte(35)
isc_dpb_old_file        = c_byte(36)
isc_dpb_old_start_page     = c_byte(37)
isc_dpb_old_start_seqno    = c_byte(38)
isc_dpb_old_start_file     = c_byte(39)
isc_dpb_drop_walfile      = c_byte(40)
isc_dpb_old_dump_id      = c_byte(41)
isc_dpb_wal_backup_dir     = c_byte(42)
isc_dpb_wal_chkptlen      = c_byte(43)
isc_dpb_wal_numbufs      = c_byte(44)
isc_dpb_wal_bufsize      = c_byte(45)
isc_dpb_wal_grp_cmt_wait    = c_byte(46)
isc_dpb_lc_messages      = c_byte(47)
isc_dpb_lc_ctype        = c_byte(48)
isc_dpb_cache_manager     = c_byte(49)
isc_dpb_shutdown        = c_byte(50)
isc_dpb_online         = c_byte(51)
isc_dpb_shutdown_delay     = c_byte(52)
isc_dpb_reserved        = c_byte(53)
isc_dpb_overwrite       = c_byte(54)
isc_dpb_sec_attach       = c_byte(55)
isc_dpb_disable_wal      = c_byte(56)
isc_dpb_connect_timeout    = c_byte(57)
isc_dpb_dummy_packet_interval = c_byte(58)
isc_dpb_gbak_attach      = c_byte(59)
isc_dpb_sql_role_name     = c_byte(60)
isc_dpb_set_page_buffers    = c_byte(61)
isc_dpb_working_directory   = c_byte(62)
isc_dpb_SQL_dialect      = c_byte(63)
isc_dpb_set_db_readonly    = c_byte(64)
isc_dpb_set_db_SQL_dialect   = c_byte(65)
isc_dpb_gfix_attach		    = c_byte(66)
isc_dpb_gstat_attach		  = c_byte(67)
isc_dpb_last_dpb_constant    = c_byte(67) # =isc_dpb_gstat_attach
isc_dpb_gbak_ods_version    = c_byte(68)
isc_dpb_gbak_ods_minor_version = c_byte(69)
isc_dpb_set_group_commit    = c_byte(70)
isc_dpb_gbak_validate      = c_byte(71)
isc_dpb_client_interbase_var  = c_byte(72)
isc_dpb_admin_option      = c_byte(73)
isc_dpb_flush_interval     = c_byte(74)
isc_dpb_instance_name	 	  = c_byte(75)


##
## Transaction parameter block stuff
##

isc_tpb_version1          = c_byte( 1)
isc_tpb_version3          = c_byte( 3)
isc_tpb_consistency       = c_byte( 1)
isc_tpb_concurrency       = c_byte( 2)
isc_tpb_shared            = c_byte( 3)
isc_tpb_protected         = c_byte( 4)
isc_tpb_exclusive         = c_byte( 5)
isc_tpb_wait              = c_byte( 6)
isc_tpb_nowait            = c_byte( 7)
isc_tpb_read              = c_byte( 8)
isc_tpb_write             = c_byte( 9)
isc_tpb_lock_read         = c_byte(10)
isc_tpb_lock_write        = c_byte(11)
isc_tpb_verb_time         = c_byte(12)
isc_tpb_commit_time       = c_byte(13)
isc_tpb_ignore_limbo      = c_byte(14)
isc_tpb_read_committed    = c_byte(15)
isc_tpb_autocommit        = c_byte(16)
isc_tpb_rec_version       = c_byte(17)
isc_tpb_no_rec_version    = c_byte(18)
isc_tpb_restart_requests  = c_byte(19)
isc_tpb_no_auto_undo      = c_byte(20)
isc_tpb_no_savepoint      = c_byte(21)
isc_tpb_last_tpb_constant = c_byte(21) # isc_tpb_no_savepoint

##
## SQL information items
##

isc_info_sql_select        = c_byte( 4)
isc_info_sql_bind          = c_byte( 5)
isc_info_sql_num_variables = c_byte( 6)
isc_info_sql_describe_vars = c_byte( 7)
isc_info_sql_describe_end  = c_byte( 8)
isc_info_sql_sqlda_seq     = c_byte( 9)
isc_info_sql_message_seq   = c_byte(10)
isc_info_sql_type          = c_byte(11)
isc_info_sql_sub_type      = c_byte(12)
isc_info_sql_scale         = c_byte(13)
isc_info_sql_length        = c_byte(14)
isc_info_sql_null_ind      = c_byte(15)
isc_info_sql_field         = c_byte(16)
isc_info_sql_relation      = c_byte(17)
isc_info_sql_owner         = c_byte(18)
isc_info_sql_alias         = c_byte(19)
isc_info_sql_sqlda_start   = c_byte(20)
isc_info_sql_stmt_type     = c_byte(21)
isc_info_sql_get_plan      = c_byte(22)
isc_info_sql_records       = c_byte(23)
isc_info_sql_batch_fetch   = c_byte(24)
isc_info_sql_precision     = c_byte(25)

##
##SQL information return values
##

isc_info_sql_stmt_select           = c_byte( 1)
isc_info_sql_stmt_insert           = c_byte( 2)
isc_info_sql_stmt_update           = c_byte( 3)
isc_info_sql_stmt_delete           = c_byte( 4)
isc_info_sql_stmt_ddl              = c_byte( 5)
isc_info_sql_stmt_get_segment      = c_byte( 6)
isc_info_sql_stmt_put_segment      = c_byte( 7)
isc_info_sql_stmt_exec_procedure   = c_byte( 8)
isc_info_sql_stmt_start_trans      = c_byte( 9)
isc_info_sql_stmt_commit           = c_byte(10)
isc_info_sql_stmt_rollback         = c_byte(11)
isc_info_sql_stmt_select_for_upd   = c_byte(12)
isc_info_sql_stmt_set_generator    = c_byte(13)


SQLDA_VERSION1	          = 1       # pre V7.0 SQLDA
SQLDA_VERSION2	          = 2       #  V7.0 SQLDA
SQLDA_CURRENT_VERSION     = SQLDA_VERSION1
SQL_DIALECT_V5	          = 1    # meaning is same as DIALECT_xsqlda
SQL_DIALECT_V6_TRANSITION = 2   # flagging anything that is delimited
                                # by double quotes as an error and
                                # flagging keyword DATE as an error
SQL_DIALECT_V6	          = 3  # supports SQL delimited identifier,
                                # SQLDATE/DATE, TIME, TIMESTAMP,
                                # CURRENT_DATE, CURRENT_TIME,
                                # CURRENT_TIMESTAMP, and 64-bit exact
                                # numeric type
SQL_DIALECT_CURRENT	      = SQL_DIALECT_V6  # (* latest IB DIALECT *)


#
# SQL datatype definitions
#
SQL_VARYING          =    448
SQL_TEXT             =    452
SQL_DOUBLE           =    480
SQL_FLOAT            =    482
SQL_LONG             =    496
SQL_SHORT            =    500
SQL_TIMESTAMP        =    510
SQL_BLOB             =    520
SQL_D_FLOAT          =    530
SQL_ARRAY            =    540
SQL_QUAD             =    550
SQL_TYPE_TIME        =    560
SQL_TYPE_DATE        =    570
SQL_INT64            =    580
SQL_DATE             =    SQL_TIMESTAMP
SQL_BOOLEAN          =    590
