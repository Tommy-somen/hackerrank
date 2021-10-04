if __name__ == '__main__':
    n = int(input())
    
    box = []
    
    for i in range(1,n+1):
        box.append(str(i))
        
    print("".join(box))
