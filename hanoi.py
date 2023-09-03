#Recursion Program

def tower_hanoi(n,a,b,c,count=0):
    count+=1
    if n==1:
        print(f"Move 1st disk from {a} to {c}")
        return 
    tower_hanoi(n-1,a,c,b)
    count+=1
    print(f'move {n} th disk from {a} to {c}')
    tower_hanoi(n-1,b,a,c)
    count+=1
    return count


def final():
    N=int(input("Enter the no of disks:"))
    print('\n')
    print(f"No of steps required to move {N} discs are {tower_hanoi(N,'s','h','d')}")
    
final()
