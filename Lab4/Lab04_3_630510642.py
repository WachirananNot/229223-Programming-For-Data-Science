#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab04_3

def prime_factorization(x):
    i = 2               
    y = x               
    while i <= x**0.5:  
        while x%i==0:   
            if x != i: 
                print(i) 
            else:      
                break   
            x = x/i     
        i += 1          
    if y == x:          
        print(x)
    else:
        print(int(x))

def main():
    x = int(input())
    prime_factorization(x)

if __name__ == "__main__":
    main()