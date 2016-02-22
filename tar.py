#!/usr/bin/env python
''' create a tar archive of current directory and save it outside '''
import tarfile
import os;
folder = os.getcwd()
s = folder.split('/')
name = s[len(s)-1]
path = '/'.join(s[0:len(s)-1])
tar = tarfile.open(path+"/archive.tar.gz", "w:gz")
tar.add(folder,arcname=name)
tar.close()
