import defaultVersion

path_to_output_file = 'output\\' #Path to Output Folder

#Function to get the file version. Accepts a list of filenames as input
#Default arguments functionality allows different invocations depending on the requirement

def get_version(location, filenames, input_sql_file='', output_csv_file=''):
	if(input_sql_file == '' and output_csv_file == ''):
		for file in filenames:
			version = defaultVersion.process_and_find_version(final_path = location, filename = file)
			print version
	else:			
		global path_to_output_file
		defaultVersion.sql_query(input_file=input_sql_file, output_file=output_csv_file)
		path_to_output_file += output_csv_file
		for file in filenames:
			data = defaultVersion.read_from_csv_file(path_to_output_file)
			version = defaultVersion.process_and_find_version(csv_input = data, final_path = location, filename = file)
			print version	
	
#Sample Invocation

#get_version(location = '%lcoation path%', filenames = '%filenames%', input_sql_file = '%input.sql%', output_csv_file = '%output.csv%')

#get_version(location = '%lcoation path%', filenames = '%filenames%')

