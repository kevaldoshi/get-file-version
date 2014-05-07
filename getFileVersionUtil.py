import subprocess
from win32api import GetFileVersionInfo, LOWORD, HIWORD
import csv
import re
import os


#Function to find the version using GetFileVersionInfo of win32api

def get_version_number (filename):
    try:
    	info = GetFileVersionInfo (filename, "\\")
    	ms = info['FileVersionMS']
    	ls = info['FileVersionLS']
    	return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
    except:
    	return 0,0,0,0
		
#A query method to execute a given query or I/O files
		
def sql_query(query='', input_file='', output_file=''):
	if(query == ''):
		input_file_path = '' #Path to input sql file
		input_file_path += str(input_file)
		output_file_path = '' #Path to output CSV file
		output_file_path += str(output_file)
		command_process = subprocess.Popen(
		['sqlcmd', '-S', '%db_name%', '-i', input_file_path, '-s', ';', '-u', '-W', '-o', output_file_path, '-h-1'],
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		)
		command_output = command_process.communicate()[0]	
	else:
		command_process = subprocess.Popen(
		['sqlcmd', '-S', '%db_name%', '-q', query, '-s', ';', '-u', '-W','-h-1'],
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		)
		command_output = command_process.communicate()[0]
		
		
#Helper function to read from a CSV file
		
def read_from_csv_file(path):
	data_initial = open( path, "rU")
	data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=";")
	return data
	
#Main logic method containing the logical calls to other helpers in sequence	
	
def process_and_find_version(final_path, filename, csv_input = ''):
	if(csv_input == ''):
		full_path_to_File = os.path.join(final_path,filename)
		version_list = get_version_number(full_path_to_File)
		version =  '.'.join(map(str,version_list))
		return version
	else:	
		requried_path = ''
		for row in csv_input:
			required_path = row[0]
			break
		number_from_path = re.findall(r'\d+', required_path)
		str_number_from_path = " ".join(str(x) for x in number_from_path)
		final_path += str_number_from_path
		full_path_to_File = os.path.join(final_path,filename)
		version_list = get_version_number(full_path_to_File)
		version =  '.'.join(map(str,version_list))
		return version
