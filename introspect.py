#! /usr/bin/env python 
import sys
import pdb
import types
import inspect
import imp

def whatsin(object, spaces=15): 
	"""Prints userdefined classes its methods and functions. Takes modules"""

	modulename = (type(object) == types.ModuleType) and object.__name__ or object;
	module = importmodule(modulename)

	objectDict = dict((name,obj) for name,obj in inspect.getmembers(module) if callable(obj))
	for name, obj in objectDict.iteritems():
		print "-".ljust(80,"-")
		prettyprint("", name, obj, spaces)
		if isinstance(obj, type):
			methodDict = dict((methodname,method) for methodname,method in
				inspect.getmembers(obj) if callable(method))
			for methodname, method in methodDict.iteritems():
				prettyprint("-->".rjust(spaces), methodname, method, spaces)
	print "-".ljust(80,"-")

def importmodule(name):
	"""Imports given module (even hierarchical module names)"""
	path = None;
	for part in name.split('.'):
		if path is not None:
			path=[path]
		file, path, descr = imp.find_module(part, path)
		res = imp.load_module(part, file, path, descr)
	return res

def prettyprint(start, name, obj, spaces):
	"""print required text prettily"""
	print '%s%s%s%s%s' % ( start, name.ljust(spaces),
			str(type(obj)).ljust(spaces) , "\n\t", 
			str(obj.__doc__).replace("\n", "\n\t").rjust(spaces))

if __name__ == "__main__":
	argv = sys.argv

	if len(sys.argv) < 2 or len(sys.argv) > 3:
		print "./introspect <module name> [spaces]"
		sys.exit(1) 

	if len(sys.argv) == 3:
		argv[2] = int(sys.argv[2]) 
	else: 
		argv.append(15);
		whatsin(argv[1], argv[2])


