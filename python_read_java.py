import os
import subprocess
from subprocess import STDOUT,PIPE

def execute_java(file_name):
    class_name,extention = os.path.splitext(file_name)
    command = ['java', class_name]
    program_execute = subprocess.Popen(command, stdin=PIPE, stdout=PIPE, stderr=STDOUT,shell=False)
    stdout,stderr = program_execute.communicate()
    return stdout

file_name="Test.java"
error=subprocess.check_call(['javac', file_name])
if error!=0:
    print "Error in code. Compile again"
else: 
    output=execute_java(file_name)
    data=output.strip()
    print data
