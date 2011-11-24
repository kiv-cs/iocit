#Configuration variable storage for iocit scripts.
#Edit it before using iocit.

#Path to images directory. Images a optional. It shows by notify-send.
img_path    = '/home/kiv/Dropbox/bin/iocit_old/img/'

#Describe target files. You may add as many files as you want.
#Set full path to file,
#image name for notifications from this file (put this image into img_path directory)
#and boolean variable 'is_shown': 'True' for show strings from this file in notifications.
target = [{'path':'/home/kiv/Dropbox/tmp/out', 'img':'0.png', 'is_shows':True},
          {'path':'/home/kiv/Dropbox/tmp/citation', 'img':'1.png', 'is_shows':True},
          {'path':'/home/kiv/Dropbox/tmp/glossary', 'img':'2.png', 'is_shows':True},
          {'path':'/home/kiv/Dropbox/tmp/googleit', 'img':'3.png', 'is_shows':True}]
