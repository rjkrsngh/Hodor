import os
import time
import logging

logging.basicConfig(filename='output.log', filemode='w', level=logging.INFO)

res = []

primary_last_mtime = 1628257247.7785158
secondary_last_mtime = 1628257268.3703601

primary_users_list = []
secondary_users_list = []

while True:
	with os.scandir('../Users/') as files_in_curr_dir:
		for file in files_in_curr_dir:
			file_stats = file.stat()
			print(file, file_stats.st_mtime)
		break
			# if file.name == 'primary_users.txt':
			# 	if primary_last_mtime != file_stats.st_mtime:
			# 		logging.info('primary file modified')
			# 		logging.info('last modification time of primary file: '.format(primary_last_mtime))
			# 		primary_last_mtime = file_stats.st_mtime
			# 		logging.info('modification time updated to : '.format(primary_last_mtime))
			# 		# UpdatePrimaryList()
			# elif file.name == 'secondary_users.txt':
			# 	if secondary_last_mtime != file_stats.st_mtime:
			# 		logging.info('secondary file modified')
			# 		logging.info('last modification time for secondary file: '.format(secondary_last_mtime))
			# 		secondary_last_mtime = file_stats.st_mtime
			# 		logging.info('modification time updated to : '.format(secondary_last_mtime))
			# 		# UpdateSecondaryList()


# Prints the epoch time in human readable format
# print(time.ctime(res[0].st_mtime))


