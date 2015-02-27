#! /usr/bin/env python
VERSION = "1.0"

import sys
import json
from optparse import OptionParser

def to_json(o, level=0):
    if level < FOLD_LEVEL:
        newline = "\n"
        space = " "
    else:
        newline = ""
        space = ""
    ret = ""
    if isinstance(o, basestring):
        o = o.encode('unicode_escape')
        ret += '"' + o + '"'
    elif isinstance(o, bool):
        ret += "true" if o else "false"
    elif isinstance(o, float):
        ret += '%.7g' % o
    elif isinstance(o, int):
        ret += str(o)
    elif isinstance(o, list):
        #ret += "[" + ",".join([to_json(e, level+1) for e in o]) + "]"
        ret += "[" + newline
        comma = ""
        for e in o:
            ret += comma
            comma = "," + newline
            ret += space * INDENT * (level+1)
            ret += to_json(e, level+1)
        ret += newline + space * INDENT * level + "]"
    elif isinstance(o, dict):
        ret += "{" + newline
        comma = ""
        for k,v in o.iteritems():
            ret += comma
            comma = "," + newline
            ret += space * INDENT * (level+1)
            #ret += '"' + str(k) + '"' + space + ':' + space
            ret += '"' + str(k) + '":' + space
            ret += to_json(v, level+1)
        ret += newline + space * INDENT * level + "}"
    else:
        #raise TypeError("Unknown type '%s' for json serialization" % str(type(o)))
        ret += str(o)
    return ret


#main():
FOLD_LEVEL = 10000
INDENT = 4

parser = OptionParser(usage='%prog json_file [options]', version=VERSION)
parser.add_option("-f", "--fold-level", action="store", type="int",
          dest="fold_level", help="int (all json is minimized to this level)")
parser.add_option("-i", "--indent", action="store", type="int",
          dest="indent", help="int (spaces of indentation, default is 4)")
parser.add_option("-o", "--outfile", action="store", type="string",
          dest="outfile", metavar="filename", help="write output to a file")
(options, args) = parser.parse_args()

if len(args) == 0:
    infile = sys.stdin
elif len(args) == 1:
    infile = open(args[0], 'rb')
else:
    raise SystemExit(sys.argv[0] + " json_file [options]")
if options.outfile == None:
    outfile = sys.stdout
else:
    outfile = open(options.outfile, 'wb')
if options.fold_level != None:
    FOLD_LEVEL = options.fold_level
if options.indent != None:
    INDENT = options.indent

with infile:
    try:
        obj = json.load(infile)
    except ValueError, e:
        raise SystemExit(e)
with outfile:
    outfile.write(to_json(obj))
    outfile.write('\n')
