#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab06_5

def check_palindrome(text):
    text = ''.join(e for e in text if e.isalnum()).lower()
    print(text)
    

def main():
    text = input()
    print(check_palindrome(text))

if __name__ == "__main__":
    main()