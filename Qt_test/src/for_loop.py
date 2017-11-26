'''
Created on 12.11.2017

@author: lukas
'''



def main():
    a=['a','k','u','i','f','x','f']
    b=[]
    c=[[],[]]
    
    
    for pos in a:
        if pos == 'f':
            b.append(pos)

    print(b)
    
    
    for idx in range(0,len(a),1):
        if a[idx] == 'f':
            c[0].append(idx)
            c[1].append(a[idx])
     
    print('Gesuchter Buchstabe {0} an Position {1}'.format(c[1][0],c[0][0]))    




if __name__ == '__main__':
    main()