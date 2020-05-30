import textwrap
from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here
    lt=textwrap.fill(string,k)
    lst=list(lt.split("\n"))
    le=len(lst)
    for i in range(0,le):
       lst[i]="".join(OrderedDict.fromkeys(lst[i]))
    for i in lst:
        print(i)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
