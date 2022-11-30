#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab05_4

def count_prime(m,n):
    count = 0
    if m>n:
        m,n = n,m

    for j in range(m,n+1):
        i = 2
        x = j
        y = j           
        while i <= x**0.5:  
            while x%i==0:   
                if x == i: 
                    break    
                x = x/i     
            i += 1          
        if y == x:          
            count +=1
    return(count)
def main():
    m,n = input("Enter m n: ").split(" ")
    print(count_prime(int(m),int(n)))

if __name__ == "__main__":
    main()