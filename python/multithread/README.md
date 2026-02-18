# MULTI-THREADED FILE SEARCHER.
## Problem statement: Security audit requires scanning thousands of fies for sensitive strings.



here is the simple program that searches for particular string  in the whole directory.and gives the output as per the format

format:  
###       directory/file_name  | line_number | particular_string snippet


-> imported necessary requirements such as threadpoolexecuter and os

-> initially we write the list of keywords which are the strings supposed to searched. 

-> particular extensions where chosen and given as a tuple.

-> and directory is chosen.

-> in that particular directory, the files with chosen extensions were searched for the keywords. (using for loop)

-> once the keyword is matched the snippet and the lineno , and the file path is given as the output. 



