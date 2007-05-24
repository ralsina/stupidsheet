from aperiot.parsergen import build_parser
myparser = build_parser('traxter')
print "A1=A1 ",myparser.parse("A1=A1")
print "A1=$A1 ",myparser.parse("A1=$A1")
print "A1=A$1 ",myparser.parse("A1=A$1")
print "A1=$A$1 ",myparser.parse("A1=$A$1")

