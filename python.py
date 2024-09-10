
shop=[{'name':'new balance', 'id': 1, 'price': 2000, 'stock': 9,'colour':'black'}, {'name': 'retro4', 'id': 2, 'price': 2000, 'stock': 10,'colour':'wight'}]
while True:
    print('''
1. add product  details
2.view product details          
3.ubdate product details
4.delete product details
5.searche product
6. exit
          ''')
    choice=int(input('enter the choice:'))
    if choice==1:
        name=str(input('enterthe shoes name:'))
        id=int(input('enter  shoes id:'))
        price=int(input('enter shoes price:'))
        stock=int(input('enter shoes stock:'))
        colour=str(input('enter shoes colour'))
        shop.append({'name':name,'id':id,'price':price,'stock':stock,'colour':colour})




    elif choice==2:
          for i in shop:
           print(i)

    elif choice==3:
        
        id=int(input('enter id:'))
        f=0
        for i in shop:
            if i['id']==id:
              while True:
                print('''
                    1.ubdate the price
                    2.ubdate the stock
                    3.exit 
                           ''')
             
                
                choice=int(input("enter your choice:"))
             
                if choice==1:
                   price=int(input("enter price:"))
                   i['price']=price
                elif choice==2:
                    stock=int(input('enter stock:'))
                    i['stock']=stock
                elif choice==3:
                    break
                else:
                    print('invalid choice')            

            f=1
            if f==0:
                print('invalid choice')
    elif choice==4:
        id=int(input('enter the id:'))
        f=0
        for i in shop:
            if i['id']==id:
              shop.remove(i)
              f=1   
        if f==0:
                 print('invalid choice')
    elif choice==5:
        id=int(input("enter id :"))
        f=0
        for i in shop:
            if i['id']==id:
                print(i)
            f=1
        if f==0:
               print('invalid id')

    
    elif choice==6:
        break
    else:
        print('invalid choice')      