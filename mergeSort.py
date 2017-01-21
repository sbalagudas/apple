#!/usr/bin/python
import sys 

class sortMethods(object):
    def __init__(self,listToBeSorted):
        if 0 != len(listToBeSorted):
            self.rawList = listToBeSorted
        else :
            self.rawList = []
            print "no data to be sorted."

    ##########################################
    #Merge Sort
    ##########################################
    def merge(self,nums,first,middle,last):
        lnums = nums[first:middle + 1]
        rnums = nums[middle + 1:last + 1]
        lnums.append(sys.maxint)
        rnums.append(sys.maxint)

        l = r = 0

        for i in range(first,last+1):
            if lnums[l] < rnums[r]:
                nums[i] = lnums[l]
                l += 1
            else :
                nums[i] = rnums[r]
                r += 1

    def mergeSort(self,first,last):
        if first < last:
            middle = (first + last) / 2
            self.mergeSort(first,middle)
            self.mergeSort(middle + 1,last)
            self.merge(self.rawList,first,middle,last)

if __name__ == "__main__":
    sortList = []
    #sortList = [1,6,4,9,0,3,5,7]
    sort = sortMethods(sortList)
    print "sortList before : ",sortList
    sort.mergeSort(0,7)
    print "sortList after : ",sortList






