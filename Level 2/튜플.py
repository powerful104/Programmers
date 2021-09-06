s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
cha1 = ','
cha2 = '}{'
s = s[2:-2]
s = ''.join(( x for x in s if x not in cha1))
s = list(s.replace(cha2," ").split())
s = [list(i) for i in s]
print(s)