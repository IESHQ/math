#!/usr/bin/env python3
import math ,re #line:2:import math, re
def addition (O0OO0OOOOO0OO0000 ):#line:4:def addition(cond):
    ""#line:9:'''
    O0OO0OOOOO0OO0000 =O0OO0OOOOO0OO0000 .replace (" ","")#line:10:cond = cond.replace(" ", "")
    O0OO0OOOOO0OO0000 =[int (OOO0O0000OOOOO0OO )for OOO0O0000OOOOO0OO in O0OO0OOOOO0OO0000 .split ('+')]#line:11:cond = [int(x) for x in cond.split('+')]
    return sum (O0OO0OOOOO0OO0000 )#line:12:return sum(cond)
def read (O0O0O0O00O0OOOOO0 ):#line:15:def read(target):
    return list (filter (None ,open (O0O0O0O00O0OOOOO0 ).read ().split ('\n')))#line:16:return list(filter(None, open(target).read().split('\n')))
class fx :#line:19:class fx:
    @staticmethod #line:20:@staticmethod
    def trigonometry (O0000O000O0O0O000 ):#line:21:def trigonometry(object):
        ""#line:26:'''
        O0000O000O0O0O000 =[OOOOOOOO0O0O0OOO0 .replace ('sin','math.sin')for OOOOOOOO0O0O0OOO0 in O0000O000O0O0O000 ]#line:27:object = [x.replace('sin', 'math.sin') for x in object]
        O0000O000O0O0O000 =[O000OOO0OOO00000O .replace ('cos','math.cos')for O000OOO0OOO00000O in O0000O000O0O0O000 ]#line:28:object = [x.replace('cos', 'math.cos') for x in object]
        O0000O000O0O0O000 =[O0000000O00O00O0O .replace ('tan','math.tan')for O0000000O00O00O0O in O0000O000O0O0O000 ]#line:29:object = [x.replace('tan', 'math.tan') for x in object]
        return O0000O000O0O0O000 #line:30:return object
    def trignometricFunctionAuto (OO000OOOO0O0OOO0O ):#line:32:def trignometricFunctionAuto(object):
        if (f'sin{i}'in OO000OOOO0O0OOO0O [z -1 ]):#line:33:if (f'sin{i}' in object[z - 1]):
            OO000OOOO0O0OOO0O =[O00OO00OOO00O0O00 .replace ('sin','math.sin')for O00OO00OOO00O0O00 in OO000OOOO0O0OOO0O ]#line:34:object = [x.replace('sin', 'math.sin') for x in object]
    @staticmethod #line:36:@staticmethod
    def translate_legacy (OO0O0OO00O0OOO0OO ,OO0O0O000OO00OO0O ):#line:37:def translate_legacy(object, z):
        ""#line:42:'''
        while OO0O0O000OO00OO0O <len (OO0O0OO00O0OOO0OO ):#line:44:while z < len(object):
            O00OO0O00O00O000O =0 #line:45:q = 0
            try :#line:47:try:
                while O00OO0O00O00O000O <len (OO0O0OO00O0OOO0OO [OO0O0O000OO00OO0O ]):#line:48:while q < len(object[z]):
                    O0O0O000OOO0OO000 =0 #line:49:i = 0
                    try :#line:51:try:
                        O00O0OO0O0O0O00O0 =[OOOOO0O0O0O000000 for OOOOO0O0O0O000000 in range (len (OO0O0OO00O0OOO0OO [OO0O0O000OO00OO0O ]))if OO0O0OO00O0OOO0OO [OO0O0O000OO00OO0O ][OOOOO0O0O0O000000 :OOOOO0O0O0O000000 +2 ]==')(']#line:52:place = [n for n in range(len(object[z])) if object[z][n:n + 2] == ')(']
                        OO0O0OO00O0OOO0OO [OO0O0O000OO00OO0O ]=f'{OO0O0OO00O0OOO0OO[OO0O0O000OO00OO0O][:O00O0OO0O0O0O00O0[O00OO0O00O00O000O] + 1]}*{OO0O0OO00O0OOO0OO[OO0O0O000OO00OO0O][O00O0OO0O0O0O00O0[O00OO0O00O00O000O] + 1:]}'#line:53:object[z] = f'{object[z][:place[q] + 1]}*{object[z][place[q] + 1:]}'
                    except IndexError :#line:55:except IndexError:
                        pass #line:56:pass
                    while O0O0O000OOO0OO000 <10 :#line:59:while i < 10:
                        try :#line:60:try:
                            O00O0OO0O0O0O00O0 =[O00O0O0O000O000OO for O00O0O0O000O000OO in range (len (OO0O0OO00O0OOO0OO [OO0O0O000OO00OO0O ]))if OO0O0OO00O0OOO0OO [OO0O0O000OO00OO0O ][O00O0O0O000O000OO :O00O0O0O000O000OO +2 ]==f'{O0O0O000OOO0OO000}(']#line:61:place = [n for n in range(len(object[z])) if object[z][n:n + 2] == f'{i}(']
                            OO0O0OO00O0OOO0OO [OO0O0O000OO00OO0O ]=f'{OO0O0OO00O0OOO0OO[OO0O0O000OO00OO0O][:O00O0OO0O0O0O00O0[O00OO0O00O00O000O] + 1]}*{OO0O0OO00O0OOO0OO[OO0O0O000OO00OO0O][O00O0OO0O0O0O00O0[O00OO0O00O00O000O] + 1:]}'#line:62:object[z] = f'{object[z][:place[q] + 1]}*{object[z][place[q] + 1:]}'
                            O00O0OO0O0O0O00O0 =[O00OO00OO0000OOOO for O00OO00OO0000OOOO in range (len (OO0O0OO00O0OOO0OO [OO0O0O000OO00OO0O ]))if OO0O0OO00O0OOO0OO [OO0O0O000OO00OO0O ][O00OO00OO0000OOOO :O00OO00OO0000OOOO +2 ]==f'){O0O0O000OOO0OO000}']#line:64:place = [n for n in range(len(object[z])) if object[z][n:n + 2] == f'){i}']
                            OO0O0OO00O0OOO0OO [OO0O0O000OO00OO0O ]=f'{OO0O0OO00O0OOO0OO[OO0O0O000OO00OO0O][:O00O0OO0O0O0O00O0[O00OO0O00O00O000O] + 1]}*{OO0O0OO00O0OOO0OO[OO0O0O000OO00OO0O][O00O0OO0O0O0O00O0[O00OO0O00O00O000O] + 1:]}'#line:65:object[z] = f'{object[z][:place[q] + 1]}*{object[z][place[q] + 1:]}'
                        except IndexError :#line:67:except IndexError:
                            pass #line:68:pass
                        O0O0O000OOO0OO000 +=1 #line:70:i += 1
                    O00OO0O00O00O000O +=1 #line:71:q += 1
                    OO0O0O000OO00OO0O +=1 #line:72:z += 1
            except IndexError :#line:74:except IndexError:
                pass #line:75:pass
    @staticmethod #line:77:@staticmethod
    def translate (O00OO0OO000O0OOO0 ,OOOO000OO0OOOO0O0 ):#line:78:def translate(object, z):
        ""#line:83:'''
        for O00O0O00OOOOOOO00 in range (10 ):#line:84:for i in range(10):
            O00OO0OO000O0OOO0 =[OOOOO0O00O00OOO00 .replace (f'{O00O0O00OOOOOOO00}(',f'{O00O0O00OOOOOOO00}*(')for OOOOO0O00O00OOO00 in O00OO0OO000O0OOO0 ]#line:85:object = [x.replace(f'{i}(', f'{i}*(') for x in object]
            O00OO0OO000O0OOO0 =[OO0OO000OO00OO0O0 .replace (f'){O00O0O00OOOOOOO00}',f')*{O00O0O00OOOOOOO00}')for OO0OO000OO00OO0O0 in O00OO0OO000O0OOO0 ]#line:86:object = [x.replace(f'){i}', f')*{i}') for x in object]
            O00OO0OO000O0OOO0 =[OOOO0O0O0O0OOOO00 .replace (f'{O00O0O00OOOOOOO00}sin',f'{O00O0O00OOOOOOO00}*sin')for OOOO0O0O0O0OOOO00 in O00OO0OO000O0OOO0 ]#line:88:object = [x.replace(f'{i}sin', f'{i}*sin') for x in object]
            O00OO0OO000O0OOO0 =[O00OOOO00O0OOO0OO .replace (f'{O00O0O00OOOOOOO00}cos',f'{O00O0O00OOOOOOO00}*cos')for O00OOOO00O0OOO0OO in O00OO0OO000O0OOO0 ]#line:89:object = [x.replace(f'{i}cos', f'{i}*cos') for x in object]
            O00OO0OO000O0OOO0 =[OO00000O0O0O0O0O0 .replace (f'{O00O0O00OOOOOOO00}tan',f'{O00O0O00OOOOOOO00}*tan')for OO00000O0O0O0O0O0 in O00OO0OO000O0OOO0 ]#line:90:object = [x.replace(f'{i}tan', f'{i}*tan') for x in object]
        O00OO0OO000O0OOO0 =[O0OOO000OOO00O0OO .replace (f'^',f'**')for O0OOO000OOO00O0OO in O00OO0OO000O0OOO0 ]#line:92:object = [x.replace(f'^', f'**') for x in object]
        return O00OO0OO000O0OOO0 #line:94:return object
    def accuFloat ():#line:96:def accuFloat():
        OOO0000OO0O0OO00O =r'[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?'#line:97:rePattern = r'[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?'
        O0O00OOOOO0OOO000 =re .compile (OOO0000OO0O0OO00O ,re .VERBOSE )#line:98:rx = re.compile(rePattern, re.VERBOSE)
        OO00OO0000000000O =O0O00OOOOO0OOO000 .findall (f"{object}")#line:99:objet = rx.findall(f"{object}")
        for OO000000OO0O0O000 in range (len (OO00OO0000000000O )):#line:100:for i in range(len(objet)):
            OO00OO0000000000O [OO000000OO0O0O000 ]#line:101:objet[i]
out =[]#line:104:out = []
def output (OOOO0O000O0OO0OO0 ):#line:105:def output(result):
    out .append (OOOO0O000O0OO0OO0 )#line:106:out.append(result)
def compile (OO0O0OO0000OOOO0O ):#line:109:def compile(target):
    ""#line:114:'''
    OO0O0O0O0OOO00000 =read (OO0O0OO0000OOOO0O )#line:116:object = read(target)
    OO00O0O0OO000OOO0 =0 #line:117:z = 0
    while OO00O0O0OO000OOO0 <len (OO0O0O0O0OOO00000 ):#line:122:while z < len(object):
        if (' calculate 'in ' '+OO0O0O0O0OOO00000 [OO00O0O0OO000OOO0 ]+' ')or (' calc 'in ' '+OO0O0O0O0OOO00000 [OO00O0O0OO000OOO0 ]+' '):#line:124:if (' calculate ' in ' '+object[z]+' ') or (' calc ' in ' '+object[z]+' '):
            output (eval (f'{OO0O0O0O0OOO00000[OO00O0O0OO000OOO0 - 1]}'))#line:125:output(eval(f'{object[z - 1]}'))
        OO00O0O0OO000OOO0 +=1 #line:127:z += 1
    if OO00O0O0OO000OOO0 ==len (OO0O0O0O0OOO00000 ):#line:129:if z == len(object):
        OO00O0O0OO000OOO0 =0 #line:130:z = 0
    while OO00O0O0OO000OOO0 <len (out ):#line:132:while z < len(out):
        print (out [OO00O0O0OO000OOO0 ])#line:133:print(out[z])
        OO00O0O0OO000OOO0 +=1 #line:134:z += 1
object =[]#line:137:object = []
def instant (OOOOO0O0O0O0O0O0O ):#line:138:def instant(input):
    ""#line:143:'''
    global object #line:145:global object
    object .append (OOOOO0O0O0O0O0O0O )#line:146:object.append(input)
    O0O00OOO0OO00O000 =0 #line:147:z = 0
    while O0O00OOO0OO00O000 <len (object ):#line:149:while z < len(object):
        if (' illegalInputTestString 'in ' '+object [O0O00OOO0OO00O000 ]+' ')or (' a@a.com 'in ' '+object [O0O00OOO0OO00O000 ]+' '):#line:151:if (' illegalInputTestString ' in ' '+object[z]+' ') or (' a@a.com ' in ' '+object[z]+' '):
            output (eval (f'{object[O0O00OOO0OO00O000 - 1]}'))#line:152:output(eval(f'{object[z - 1]}'))
        if 'calc'==object [O0O00OOO0OO00O000 ]:#line:154:if 'calc' == object[z]:
            object =fx .translate (object ,O0O00OOO0OO00O000 )#line:155:object = fx.translate(object, z)
            object =fx .trigonometry (object )#line:156:object = fx.trigonometry(object)
            output (eval (f'{object[O0O00OOO0OO00O000 - 1]}'))#line:158:output(eval(f'{object[z - 1]}'))
        O0O00OOO0OO00O000 +=1 #line:160:z += 1
    if O0O00OOO0OO00O000 ==len (object ):#line:163:if z == len(object):
        O0O00OOO0OO00O000 =0 #line:164:z = 0
    while O0O00OOO0OO00O000 <len (out ):#line:166:while z < len(out):
        print (out [O0O00OOO0OO00O000 ])#line:167:print(out[z])
        O0O00OOO0OO00O000 +=1 #line:168:z += 1
        object .clear ()#line:169:object.clear()
        out .clear ()#line:170:out.clear()
live =1 #line:173:live = 1
written =0 #line:174:written = 0
while live ==1 :#line:176:while live == 1:
    try :#line:177:try:
        x =input ('> ')#line:178:x = input('> ')
        if x :#line:179:if x:
            instant (x )#line:180:instant(x)
    except IndexError or ValueError :#line:182:except IndexError or ValueError:
        print ("Fix inserted formula")#line:183:print("Fix inserted formula")
    except NameError :#line:185:except NameError:
        object .clear ()#line:186:object.clear()
        print ('No value returned')#line:187:print('No value returned')
while written ==1 :#line:190:while written == 1:
    compile ('test.math')#line:191:compile('test.math')
    break #line:192:break
print (str (fx .accuFloat ))