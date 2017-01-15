SNORT_RULE_PATH = '/etc/snort/rules/local.rules'
SNORT_CONF_PATH = '/etc/snort/snort.conf'
INTERFACE = 'eth0'
TABLE_WORD = {
	'udp' = ['sid', 'cid', 'udp_sport', 'udp_dport', 'udp_len', 'udp_csum'],
	'tcp' = ['sid', 'cid', 'tcp_sport', 'tcp_dport', 'tcp_seq', 'tcp_ack', 'tcp_off', 'tcp_res', 'tcp_flags', 'tcp_win','tcp_csum', 'tcp_urp']
}
MYSQL_USER = 'snort'
MYSQL_HOST = 'localhost'
MYSQL_PASSWD = '123456'
DB_NAME = 'snort'