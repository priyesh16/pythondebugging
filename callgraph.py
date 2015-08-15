#!/usr/bin/env python

import sys
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

from introspect import whatsin 

graphviz = GraphvizOutput(output_file='callgraph.png')

with PyCallGraph(output=graphviz):
	whatsin(sys.argv[4])
