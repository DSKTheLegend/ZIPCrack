import sys
import zipfile
import optparse
from threading import Thread

def extractFile(zFile, password,verbose):
    try:
        zFile.extractall(pwd=password)
        print('[+] Brute Force Successful : ' + password)
        return password
    except:
        if verbose is True:
            print('[*] Brute Force Failed : ' + password)
          
        return
def main():
    parser = optparse.OptionParser('usage: zipcracker.py ' + '-f <zipfile> -w <wordlist>')
    parser.add_option('-f', dest='zname',type='string',help='specify zip file')
    parser.add_option('-w', dest='wname',type='string',help='specify wordlist file')
    parser.add_option('-v', dest='verbose',type='string',nargs=0,help='verbose')
    (options,args) = parser.parse_args()
    if (options.zname == None) | (options.wname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        wname = options.wname
    if options.verbose == None :
            verbose = False
    else:
            verbose = True 
    try:
        zFile = zipfile.ZipFile(zname)
    except:
        print("The ZIP file you provided cannot be loaded! ")    
    try:
        passFile = open(wname)
    except:
        print("The wordlist you provided cannot be loaded!")    
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password,verbose))
        t.start()

if __name__ == '__main__':
    load = """
    ZZZZZ   IIIIII  PPPPPP       CCCCC  RRRR      A     CCCCC  K  K
        z     i     p     p      c      r   R    A A    c      k k  
      z       i     pppppp  |||  c      r R     A   A   c      kk  
    z         i     p            c      r  R   AaaaaaA  c      k k
    ZZZZZ   IIIIII  p            CCCCC  R   R  A     A  CCCCC  K  K 
    """
    print(load)
    main()
