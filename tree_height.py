#221RDB527 Vjačeslavs Meļņičenko 15.grupa
#python3

import sys
import threading
import numpy

def compute_height(n, parents):
    u = n*[-1]
    def h(node):
        if u[node] != -1:
            return u[node]
        if parents[node] == -1:
             u[node] = 1
        else:
             u[node] = h(parents[node])+1
        return  u[node]
   
    max_height = 0
    
    for root in range(n):
        max_height = max(max_height,h(root))
        
    return max_height


def main():
    
    tx = input("I or F: ")
    if "I" in tx:
       n = int(input())
       parents = list(map(int, input().split()))
    elif "F" in tx:
        c = input()
        ts ='./test/'
        fl = ts+c
        
        if "a" not in c:
            try:
                with open(fl) as x:
                    n=int(x.readline())
                    parents=list(map(int,x.readline().split()))
            except Exception as y:
                print("Error",str(y))
                return
            
        else:
            print("Error")
            return    
    print(compute_height(n,parents))    
    
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
