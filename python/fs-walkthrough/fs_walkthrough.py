#!/usr/bin/python
import os
import sys
import pprint

class FSanalytics(object):
class FS(object):
    def __init__(self, name):
        self.name = name

    def get_files_dir(self, path=None):
        if path is None:
            path = self.name
        files = []
        files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
        return files

    def get_dirs_dir(self, path=None):
        if path is None:
            path = self.name
        dirs = []
        dirs = [file for file in os.listdir(path) if os.path.isdir(os.path.join(path, file))]
        return dirs

    def get_file_stats(self, path=None):
        files = {}
        data = {}
        if path is None:
            path = self.name
        for filename in os.listdir(path):
            filename = os.path.join(path, filename)
            files[filename] = posix2dict(os.stat(filename))
            if os.path.isfile(filename):
                files[filename]['type'] = 'file'
            elif os.path.isdir(filename):
                files[filename]['type'] = 'dir'
            else:
                files[filename]['type'] = ['link']
        """
        for root, dirs, files in os.walk(path):
            #import pdb;pdb.set_trace()
            data[root] = {}
            data[root]['dirs'] = dirs
            data[root]['files'] = files
        return data
        """
        return files

    def get_dir_stats(self, path=None):
        if path is None:
            path = self.name
        parent_d = {}
        for idir in self.get_dirs_dir(path=path):
            idir = os.path.join(path,idir)
            parent_d[idir] = self.get_file_stats(idir)
        return parent_d

    def list_files(self, path=None):
        if path is None:
            path = self.name
        for root, dirs, files in os.walk(path):
            level = root.replace(path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))

def posix2dict(stats):
    d = {}
    d['st_mode'] = stats.st_mode
    d['st_ino'] = stats.st_ino
    d['st_dev'] = stats.st_dev
    d['st_nlink'] = stats.st_nlink
    d['st_uid'] = stats.st_uid
    d['st_gid'] = stats.st_gid
    d['st_size'] = stats.st_size
    d['st_atime'] = stats.st_atime
    d['st_mtime'] = stats.st_mtime
    d['st_ctime'] = stats.st_ctime
    return d

fs = FS(sys.argv[1])
pprint.pprint(fs.get_file_stats())
