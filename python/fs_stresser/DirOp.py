import sys
import os
import shutil
import string
import random
from multiprocessing import Pool


def id_generator(size=120, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class DirOp(object):
    def __init__(self):
        self.dir_list = []
        self.workdir = ""

    def create_dir(self, num=1, nthreads=1, path="./", name_len=120):
        self.workdir = path
        if not os.path.exists(path):
            os.makedirs(path)
        self.dir_list = [ path + "/" +id_generator(size=name_len) for x in xrange(0, num)]
        p = Pool(nthreads)
        p.map(os.mkdir,self.dir_list)

    def delete_dir(self, pattern=None, all_dirs=False,path=None, count=1):
        del_list = []
        if pattern ==  "alternate":
            del_list = self.dir_list[::2]
            self.dir_list[:] = [item for item in self.dir_list if item not in del_list]
        elif pattern ==  "random":
            del_list = [random.choice(self.dir_list) for x in xrange(0,count)]
            self.dir_list[:] = [item for item in self.dir_list if item not in del_list]
        elif pattern ==  "subarray":
            for x in xrange(0,count-5):
                index = random.choice(len(self.dir_list)-1)
                for index in xrange(index, index+5):
                    self.dir_list[:].pop(index)
        if all_dirs:
            del_list = self.dir_list
            self.dir_list = []
            shutil.rmtree(self.workdir)
        else:
            for item in del_list:
                shutil.rmtree(item)

    def create_hardlink(self):
        pass

    def create_softlink(self):
        pass

    def rename_dir(self, pattern=None, path=None, count=1):
        rename_list = []
        new_names = []
        if pattern ==  "alternate":
            rename_list = self.dir_list[::2]
            self.dir_list[:] = [item for item in self.dir_list if item not in rename_list]
        elif pattern ==  "random":
            rename_list = [random.choice(self.dir_list) for x in xrange(0,count)]
            self.dir_list[:] = [item for item in self.dir_list if item not in rename_list]
        new_names = [ self.workdir + "/" +id_generator(size=120) for x in xrange(0, len(rename_list))]
        for old, new in zip(rename_list, new_names):
            os.rename(old,new)
        self.dir_list[:].append(new_names)

if __name__ == "__main__":
    d = DirOp()
    d.create_dir(num=1000,nthreads=4,path="./testpath")
    d.delete_dir(pattern="alternate",count=50)
    d.delete_dir(pattern="random",count=5)
    d.rename_dir(pattern="alternate", count=4)
    d.create_dir(num=1000,nthreads=4,path="./testpath")
    d.delete_dir(all_dirs=True)
