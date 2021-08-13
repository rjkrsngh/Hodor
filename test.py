# from pynput.keyboard import Key, Listener, Controller
  
# # 	Capture key press
# def show(key):
  
#     print('\nYou Entered {0}'.format( key))
  
#     if key == Key.delete:
#         # Stop listener
#         return False
  
# # Collect all event until released
# with Listener(on_press = show) as listener:   
#     listener.join()

# Need to run a long test for verification

# import ctypes
# ctypes.windll.user32.LockWorkStation()

# import ctypes
# import time

# count = 0
# while count<10000000:
#     res = ctypes.windll.User32.GetForegroundWindow()
#     if res%10 == 0:
#         print('res: {} at time: {}'.format(res, time.asctime()))
#     # time.sleep(1)
#     count+=1



#Perfect Program
# import subprocess as s
# import time
# # time.sleep(5)

# def func():
#     process_name='LogonUI.exe'
#     callall='TASKLIST'

#     while(True):
#         outputall=subprocess.check_output(callall)
#         outputstringall=str(outputall)
#         if process_name in outputstringall:
#             print("Locked ", time.asctime())
#         else: 
#             print("Unlocked ", time.asctime())
#             break

# def testFunc():
#     print('printing from testFunc')



