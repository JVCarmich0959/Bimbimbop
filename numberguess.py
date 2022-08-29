def main():
        smaller=int(input("Enter the smaller number: "))
        larger=int(input("Enter the larger number: "))
        low=smaller
        high=larger
        cnt=0
        while low<=high:
            mid=(low+high)//2;
            cnt=cnt+1
            print("Your number is ",mid)
            c=input("Enter =,<, or >:")
            if c=='=':
                print("Hooray,I've got it in ",cnt,"tries!")
                return 1 #meaning true
            elif c=='>':
                low=mid+1
            else:
                high=mid-1
        return 0 #meaning false
    
t = main()
if t==0:
    print("You're cheating!")
