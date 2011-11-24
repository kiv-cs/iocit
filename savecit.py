#!/usr/bin/python
import sys
import os
import subprocess
import config
#/TODO ignore ' and " in input string

is_ret = True
target_num = 0
args = sys.argv[1:]
if len(args)>0:
    if '-t' in args:
        is_ret = False
    if '-s' in args:
        target_num = int(args[args.index('-s') + 1])
output_path = config.target[target_num]['path']
img = config.target[target_num]['img']
title = output_path.split('/')[-1].upper()

def get_xsel_input():
    in_content = subprocess.check_output(['xsel','-p'])
    return in_content

def clear_input(in_content):
    in_string = in_content.replace('\t','  ')
    in_string = in_string.replace('\n', '\t')
    return in_string

def save_content(out_path, in_string, is_ret):    
    #there must be a easer way to add a string in the end of a file! 
    outfile = open(out_path, 'r')
    in_content = outfile.read()
    outfile.close

    in_content+=in_string
    if is_ret:
        in_content+='\n'
    else:
        in_content+='\t'

    outfile = open(out_path, 'w')
    outfile.write(in_content)
    outfile.close

def notify_send(title, saved_string, is_ret):
    if not is_ret:
        saved_string = '^fg(red)' + saved_string
    output = 'echo \"->{1}: {0}\"'.format(saved_string, title)
    subprocess.Popen([output + '| dzen2 -p 2 -w 400 -h 30 -ta r -x 800 -y 100 -l 3 -fg green'], shell=True)

in_content = get_xsel_input()
in_string = clear_input(in_content)
save_content(output_path, in_string, is_ret)
notify_send(title, in_string, is_ret)
