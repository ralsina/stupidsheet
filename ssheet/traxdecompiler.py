def regurgitate(assignlist):
        '''Takes an assignlist (the output of the trax parser)
        and produces traxter code.'''
        for assignment in assignlist:
                print assignment


if __name__=="__main__":
        from aperiot.parsergen import build_parser
        traxparser = build_parser('traxter')
        t='A1=SUM(A1:A7);'
        pprint (regurgitate(traxparser.parse(t)))
        print
        print
        t='A1=SUM(AVG(A1:A7))*2;'
        pprint (decompile(traxparser.parse(t)))
        print
        print
        t='A1=$A1+A$1+$A$1+A1;'
        pprint (decompile(traxparser.parse(t)))
