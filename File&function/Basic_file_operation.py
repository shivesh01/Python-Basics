f=open('hello.txt','w')                            #opens a filename exit either creates one     #mode defined and encoding type is defined
f.close()                                          #closing a file (sometimes this doesn"t work)
with open("hello.txt",encoding = 'utf-8') as f:    #file closing(always works!)