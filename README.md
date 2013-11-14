path-to-timestamp
=================

python script that modifies timestamp based on system path. It will take /my/path 
and traverse all files through the os.walk function. When it encounters a file
it will apply to date formats to the filename to determine the date.

Example:
020212test.html would be modified so the modification and access date would be 2012-02-02.

Example usage:
$ python run.py /my/path
