#!/usr/bin/env python
# 
# Copyright 2013 Eric Gustafson
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0
# 
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
# 
import dns.resolver
import sys

rec_stack = sys.argv[1:]

while len(rec_stack) > 0:
    fqdn = rec_stack.pop()
    try:
        print "# %s" % (fqdn)
        answers = dns.resolver.query(fqdn, 'TXT')
        for rdata in answers:
            fields = rdata.to_text().split()
            for f in fields:
                if f.find(":") > -1 :
                    k,v = f.split(":",1)
                    if ( k == 'include' ):
                        rec_stack.append( v )
                    if ( k == 'ip4' ):
                        print v
                    if ( k == 'a' ):
                        ans = dns.resolver.query(v, 'A')
                        for rd in ans:
                            print rd.address
    except dns.resolver.NoAnswer:
        None

