get-file-version
================

A python script to get the version of a given file.

Operates two ways - 

1) Given the path and a list of filenames, it returns the version of the files

2) Given a sql query to extract a location value, it parses the value for a number and substitues the number to form a path for the file.

eg - given the value in DB is 'my-folder/version_12345', it parses this value to find 90234

     Substitues this value to form the actual path to file - 'remote-folder/release/version/12345'
     
     Finds the version of files andreturns them in the format 1.23.4.5 --according to actual representation
