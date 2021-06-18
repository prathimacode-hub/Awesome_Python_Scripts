def TowerofHanoi(n,from_rod,to_rod,middle_rod):
    if n==1:
        print("Move disk 1 from",from_rod,"to",to_rod)
        return
    TowerofHanoi(n-1,from_rod,middle_rod,to_rod)
    print("Move disk",n,"from",from_rod,"to",to_rod)
    TowerofHanoi(n-1,middle_rod,to_rod,from_rod)

    
n=int(input("Enter number of disks:"))
TowerofHanoi(n,'A','C','B')