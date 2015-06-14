# import os , time , mmap
#mm= list ()
#mmap=mmap.mmap(-1,11)
 pid= os.fork()
 if pid!=0:
 mm [o:-1]="hola mundo"
 os.waitpid (pid, o)
 print "mm en el padre", mm [:-1]
 else:
 time.sleep(1)
 print "mm en el hijo",mm [:-1]

