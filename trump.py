

import requests
url = 'https://www.vox.com/2018/9/25/17901082/trump-un-2018-speech-full-text'
r = requests.get(url)
d = str(r.text)
d=d[92005:117345]
n = d.lower()
words=n.split( )
n=n.replace(',',' ')
n=n.replace('.',' ')
n=n.replace('’',' ')
n=n.replace("</p>"," ")
n=n.replace('<p',' ')
n=n.replace('</p>',' ')
n=n.replace('id=', ' ')
n=n.replace('\n',' ')
n=n.replace('[',' ')
n=n.replace(']',' ')
n=n.replace('>',' ')
n=n.replace('<',' ')
n=n.replace('(',' ')
n=n.replace(')',' ')
n=n.replace('“',' ')
n=n.replace('”',' ')
n=n.replace('’s',' ')
n=n.replace('’s ',' ')
n=n.replace("'s "," '")
n=n.replace('"',' ')
n=n.replace("'"," ")
n=n.replace('–',' ')
n=n.replace('-',' ')
mydict = {}
for w in words:
         if w in mydict:
                  mydict[w] +=1
         else:
                  mydict[w] = 1
r=sorted(mydict,key=mydict.__getitem__,reverse=True)
for k in r[:20]:
    print('%s : %s' %(k, mydict[k]))
