import os
import sys
import time
import logging
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Not required as of now
# from watchdog.events import LoggingEventHandler

folder_to_track = 'C:/Users/raj/Desktop/Dev/IMHodor/Users'
primary_users_list = []
secondary_users_list = []

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        # print('folder modified', event)
        # print(event.event_type) # returns the type of event
        # print(event.src_path) # returns the path of the modified file
        # for file_name in os.listdir(folder_to_track):
        #     src = folder_to_track + '/' + file_name

        FileName = self.GetFileNameFromPath(event.src_path)
        if FileName == 'primary_users.txt':
            print('Primary file changed!')
            self.GenerateNewPrimaryUsersList()
        elif FileName == 'secondary_users.txt':
            print('secondary file changed!')
            self.GenerateNewSecondaryUsersList()

    def GetFileNameFromPath(self, path):
        print('Extracting file name')
        user_platform = os.name
        if user_platform == 'nt':
            return path[path.rfind('\\')+1:]                                                                                                                                                                                                                   
        elif user_platform == 'posix': 
            return path[path.rfind('/')+1:]  

    ################################################################################
    # Move these 2 functions to a separate file
    def GenerateNewPrimaryUsersList(self):
        print('Generating primary users list')
        os.chdir('Users')
        with open('primary_users.txt', 'r') as f:
            allUsers = f.readlines()
            for user in allUsers:
                primary_users_list.append(user.strip())

        print(primary_users_list)
        return

    def GenerateNewSecondaryUsersList(self):
        print('Generating secondary users list')
        os.chdir('Users')
        with open('secondary_users.txt', 'r') as f:
            allUsers = f.readlines()
            for user in allUsers:
                secondary_users_list.append(user)

        print(secondary_users_list)
        return

    ##################################################################################

observer = Observer()
EventHandler = Handler()

observer.schedule(EventHandler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        #Check every 3 seconds
        time.sleep(3)
except KeyboardInterrupt:
    Observer().stop()
finally:
    # join the thread
    Observer().join()





########################## TO MONITOR MULTIPLE FOLDERS #############################

# import multiprocessing

# def monitor_folder(folder):
#     observer.schedule(EventHandler, folder_to_track, recursive=True)
#     observer.start()

#     try:
#         while True:
#             time.sleep(3)
#     except KeyboardInterrupt:
#         Observer().stop()
#     finally:
#         Observer().join()

# if __name__ == '__main__':
#     m1 = multiprocessing.Process(target=monitor_folder, args=(folder1,))
#     m2 = multiprocessing.Process(target=monitor_folder, args=(folder2,))

#     m1.start()
#     m2.start()
