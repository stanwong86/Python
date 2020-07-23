'''Given the following input in a file and the python code below:

Received: from ghostbusters.mr.itd.umich.edu (ghostbusters.mr.itd.umich.edu [141.211.93.144])
by panther.mail.umich.edu () with ESMTP id m04LAcZw014275;
Fri, 4 Jan 2008 16:10:38 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
by paploo.uhi.ac.uk (Postfix) with ESMTP id C48CDBB490;
Fri,  4 Jan 2008 21:10:31 +0000 (GMT)

PYTHON CODE
import re
fhand = open('mbox-short.txt')
for line in fhand:   
       line = line.rstrip()   
       addr = #Regular expression goes here
       if len(addr) > 0 :
             print(addr)
             
Provide the regular expression that extracts from each "Received: from" lines, the first mail server name
(Example: 'paploo.uhi.ac.uk').  The search only needs to search lines with lowercase 'from'
'''

import re
fhand = open('mbox-short.txt')
for line in fhand:   
       line = line.rstrip()
       # m = re.search(r'\b[\w.-]+?@\w+?\.\w+?\b', line)
       m = re.search(r'From: (.*@.*\..*)[\s\n]?', line)
       if m:
       	addr = m.group(1)
       else:
       	addr = ""
       if len(addr) > 0 :
             print(addr)