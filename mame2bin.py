"""
mame2bin, by Parzival Wolfram <parzivalwolfram@gmail.com>

Program released under the MIT license, see https://opensource.org/licenses/MIT
or https://web.archive.org/web/20220726165438/https://opensource.org/licenses/MIT

Usage: mame2bin <input dump> <output binary>

this takes the MAME text hex dump format, eg:

0000:  00 00 F3 C3 15 00 25 00 DD 2B DD 70 00 DD 2B DD  ......%..+.p..+.
0010:  71 00 C1 FD E9 F3 ED 46 01 F4 00 ED 41 79 D6 01  q......F....Ay..
0020:  4F D2 1B 00 3E 01 D3 08 01 15 00 ED 78 0E 14 ED  O...>.......x...
etc.

and converts to a raw dump, which can be manipulated in a hex editor or similar.
I tried to keep this short and sweet, as it has a very simple job to do.

"""

from binascii import unhexlify
from sys import argv


helpflags = ["--help","-help","-?","/?","/help","-h"] #this is literally only for the below block


for i in helpflags: #this only triggers for "mame2bin <a help flag>" or just "mame2bin", but whatever
        if argv[-1] == i: #is there a help flag in the last position? 
                print(" ".join(argv[0:len(argv)-1])+" <input hex dump> <output binary>")
                exit(0)
        elif "mame2bin" in argv[-1]: #did you provide no filenames?
                print(" ".join(argv)+" <input hex dump> <output binary>")
                exit(0)


try: #open input file
        fileIn = open(str(argv[-2]),"r")
except IOError:
        print("Input file does not exist!")
        exit(1)


try: #open output file
        fileOut = open(str(argv[-1]),"wb+")
except IOError:
        print("Cannot create output file!")
        exit(2)


fileLineList = fileIn.readlines()
fileIn.close() #close input file, as we don't really need it open if it's been copied to the above list in RAM, do we?
#i might add a flag to just convert the file one line at a time from disk at some point

outbuf = b""
for i in fileLineList:
        endflag = False #dirty way of doing this, but w/e
        loopbuf = i.split(" ")
        del loopbuf[0] #strip the address portion
        del loopbuf[0] #strip the empty split that consists of just a space, or since it's been split, an empty string
        for j in loopbuf:
                if endflag != True:
                        if j == "":
                                endflag = True
                        else:
                                outbuf += unhexlify(j) #this is literally 80% of the functionality of this script.


try:
        fileOut.write(outbuf)
except IOError:
        print("Cannot write to output file!")
        exit(3)
fileOut.flush() #on some systems and python versions, but not all, just closing without manually flushing will discard all writes you've done to the file.
fileOut.close()
