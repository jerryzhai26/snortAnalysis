import subprocess
import logging
from GlobalDef import *
class SnortOP(object):
	"""docstring for ClassName"""
	def __init__(self, rulefile = SNORT_RULE_PATH, workpath):
		self.rulefile = rulefile
		self.workpath = workpath
		self.logger = get_logger()
		
	def mod_local_rules(self, rule):
		with open(self.rulefile,'a') as fr:
			fr.write(snortRules + '\n')

	def restart_snort(self):
		stop_snort()
		start_snort()

	def stop_snort(self):
		stop_cmd = 'sh -x %s/stop_snort.sh' %self.workpath
		self.logger.info(stop_cmd)
		subprocess.call(stop_cmd, shell = True)

	def start_snort(self):
		start_cmd = 'snort -i %s -c %s  -D' %(INTERFACE, SNORT_CONF_PATH)
		self.logger.info(start_cmd)
		subprocess.call(stop_cmd, shell = True)

    def get_logger(self):

        logfilename = '%s/testMethod.log' % (self.workpath)

        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(filename)s:%(lineno)d : %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filemode='w')

        logger = logging.getLogger('OperationSnort')

        # file_hander = logging.FileHandler('%s/nosetest.log' %(self.env.wksp))
        file_hander = logging.FileHandler(logfilename,  mode='w')
        file_hander.setLevel(logging.INFO)
        file_formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(filename)s:%(lineno)d : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_hander.setFormatter(file_formatter)

        logger.addHandler(file_hander)

        # console printing
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # console formatter
        formatter = logging.Formatter(
            '%(asctime)s: %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        console.setFormatter(formatter)
        logger.addHandler(console)

        return logger