# random        it’s a built-in web server
# collections   processes a comma-delimited file of text
# os            lets you interact with your underlying operating system
# itertools     can generate numbers in an unpredictable order
# http.server   reports on a file’s modification date, for instance
# pdb           this module let’s you test your code one function at a time
# pprint        provides a bunch of advanced data types
# csv           popular structured text format, sometimes call a “document”
# stat          digital certs and encrypted connections rely on this module
# unittest      this does the trick when your output needs to be pretty
# re            for all your advanced looping needs
# enum          you can use this to debug your Python code
# ssl           if your data’s compressed in a file, this module’s got your back
# json          a regular expression library (not “line noise”)
# sys           the world’s most popular embedded relational database system
# zipfile       a set of typed named values
# sqlite3       tells you all about the system you’re running on
import os
import sys
from pprint import pprint

print( "http.server",  "=", "it’s a built-in web server")
print( "csv",  "=", "processes a comma-delimited file of text")
print( "os",  "=", "lets you interact with your underlying operating system")
print( "random",  "=", "can generate numbers in an unpredictable order")
print( "stat",  "=", "reports on a file’s modification date, for instance")

print( "unittest",  "=", "this module let’s you test your code one function at a time")
print( "collections",  "=", "provides a bunch of advanced data types")
print( "json",  "=", "popular structured text format, sometimes call a “document”")
print( "ssl",  "=", "digital certs and encrypted connections rely on this module")
print( "pprint",  "=", "this does the trick when your output needs to be pretty")

print( "itertools",  "=", "for all your advanced looping needs")
print( "pdb",  "=", "you can use this to debug your Python code")
print( "zipfile",  "=", "if your data’s compressed in a file, this module’s got your back")
print( "re",  "=", "a regular expression library (not “line noise”)")
print( "sqlite3",  "=", "the world’s most popular embedded relational database system")

print( "enum",  "=", "a set of typed named values")
print( "sys",  "=", "tells you all about the system you’re running on")


print (sys.version_info, sys.platform, sys.version)
print (os.name)
