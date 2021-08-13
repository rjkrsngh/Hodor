import os
import time
import subprocess
import cv2 as cv
import face_recognition.api as face_recognition

camera = None

# TODO: Use proper design patterns

def captureImage(image_count):
	# print('pwd:',os.getcwd())
	
	# while(True):
		# Store only last 100 captures
	if image_count>100:
		image_count = 1

	ret, image = camera.read()
	imageName = 'webcam'+str(image_count)+'.jpg'

	# print('current directory is: {}'.format(os.getcwd()))

	if os.path.exists(imageName):
		print('Image with this name already exists.') 

		cmd = '' # stores the command to remove the already existing file

		# os.name helps us detect the operating system
		# returns 'nt for windows', 'posix for mac/linux'

		user_platform = os.name
		if user_platform == 'nt':
			cmd = 'del '+imageName
		elif user_platform == 'posix': 
			cmd = 'rm -f '+imageName
			
		print('removing existing file', imageName)
		os.system(cmd)

	print('Making a fresh write for', imageName)
	cv.imwrite(imageName, image)
	print('total images captured :', image_count)
	# time.sleep(5)
	print('capturing next image...')

	# camera.release()
	# cv.destroyAllWindows()

if __name__ == '__main__':
	
	process_name='LogonUI.exe'
	task_list='TASKLIST'

	num_of_images = 0
	
	# Navigate to the unknown directory
	os.chdir('unknown')
	
	while True:
		out = subprocess.check_output(task_list)
		allProcOut = str(out)
		
		# Indicates that the screen is locked
		while process_name in allProcOut:
			# os.system('TASKLIST > running_processes.txt')

			if not camera:
				print('Initializing a new instance of webcam...')
				camera = cv.VideoCapture(0)
			print('window is locked: {}'.format(time.asctime()))
			#print('output when window is locked: {}'.format(allProcOut))
			
			num_of_images += 1
			captureImage(num_of_images)
			time.sleep(1)
			if num_of_images > 100:
				num_of_images = 0

			out = subprocess.check_output(task_list)
			allProcOut = str(out)	        
		else: 
			# res = 'unlocked'
			print('Unlocked: {}'.format(time.asctime()))
			#print('output when unlocked: {}'.format(allProcOut))
			
			if camera:
				print('releasing camera')
				camera.release()
				cv.destroyAllWindows()	
				camera = None		



