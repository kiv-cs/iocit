#!/usr/bin/python
# -*- coding: utf-8 -*-

#This program is free software. It comes without any warranty, to
#the extent permitted by applicable law. You can redistribute it
#and/or modify it under the terms of the Do What The Fuck You Want
#To Public License, Version 2, as published by Sam Hocevar. See
#http://sam.zoy.org/wtfpl/COPYING for more details.

#script extracts set of tabulated values from file
from random import choice
import subprocess
import config

def notify_send(title, content, img):
    subprocess.call(['notify-send', '-t', '3000', '-i', img ,title, content])    
target = choice(config.target)
title = target['path'].split('/')[-1].upper()
img = config.img_path + target['img']

file = open(target['path'], 'r')
filecontent = file.read()
#check if any string is empty
i = 0
for i in range(0,50):
    rand_str = choice(filecontent.split('\n'))
    if rand_str == '':
        continue
    content = rand_str.replace('\t', ': \n')
    notify_send(title, content, img)
    break
file.close()
