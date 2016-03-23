#!/usr/bin/env python
# -*- coding: utf8 -*-
# bk_mysql @ Python
# Functions: 
# Created By HavenShen on 2016-03-23,Version 0.1

import sys,os,time,subprocess

file_name = 'bug.md'
file_path = '/Users/HavenShen/Desktop/gogit/'

def check_file():
	if not os.path.exists(file_path + file_name):
		f = open(file_path + file_name,'w')
		f.write(str(time.time()) + '\n')
		f.close()

def add_file_line():
	f = open(file_path + file_name,'a+')
	f.write(str(time.time()) + '\n')
	f.close()


def cmd_list():
	cmd_list = []
	cmd_list.append("git add .")
	cmd_list.append("git commit -m 'first commit" + str(time.time()) + "'")
	cmd_list.append("git push -u origin master")
	return cmd_list
	
def cmd_go():
	cmd_str_list = cmd_list()
	for cmd_go in cmd_str_list:
		subprocess.call(cmd_go,shell=True)

def file_handle():
	check_file()
	add_file_line()
	cmd_go()


if __name__ == "__main__":
	file_handle()
	print 'ok'