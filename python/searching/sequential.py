#!/usr/bin/python

class SequentialSearcher(object):
    def __init__(self):
            print "SequentialSearcher Object initialized."
            self.item_list =  list()

    def __init_(self, input):
        print "SequentialSearcher Object initialized with parameters."
        self.item_list = input

    def search(self, key):
        print("Array:%s\n"% self.item_list)
        print("SearchKey: %s\n"%key)
        if len(self.item_list) is 0:
            return -1
        else:
            if key in self.item_list:
                return self.item_list.index(key)+ 1

if __name__ == "__main__":
    s = SequentialSearcher()
    s.item_list = [1,2,3,4,5,6,7,8]
    print s.search(4)
