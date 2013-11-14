path-to-timestamp
=================

python script that modifies timestamp based on system path. It will take /my/path 
and traverse all files through the os.walk function. When it encounters a file
it will apply to date formats to the filename to determine the date.

Example:
020212test.html would modify the modification and access date to be 2012-02-02.

$ python run.py /my/path
