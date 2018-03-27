movenum=0
def hanoi(n, source, helper, target):
    global movenum
    #print "Source= "+source+", helper= "+helper +", target= "+target  
    if n==1:
        movenum+=1
        print ("Move# "+str(movenum)+": Move top most ring from "+source+"(source) to "+target+"(target)")
        return
    else:
        # move tower of size n - 1 to helper(not orignal variable in main but helper variable at this point)
        hanoi(n - 1, source, target, helper)
        # move disk from source to target(not orignal variables in main but src n target variables at this point)
        movenum+=1
        print ("Move# "+str(movenum)+": Move top most ring from "+source+"(source) to "+target+"(target)")
        # move tower of size n-1 from helper to target(not orignal variables in main but helper n target variables at this point)
        hanoi(n - 1, helper, source, target)

if __name__ == '__main__':
    source = "peg1"
    target = "peg3"
    helper = "peg2"
    hanoi(5,source,helper,target)