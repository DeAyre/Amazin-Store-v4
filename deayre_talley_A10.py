import os # include this import only if not done elsewhere in your code

def itemMenu (category, itemList):
    """itemMenu function - displays menu of variable number of shopping items.
       Inputs: category (books, etc.), list of item descriptions and prices.
       Returns: selected menu item (integer, 1 to n), s, or x
       ---------------------------------------------------------------------"""  
    os.system('cls')
    print ('\n\n\t\t ' + category + ' menu')
    print ('\n\t\t Select from the following items, display cart, or checkout: ')
    print('\n\t\t\t {0:3s}  {1:26s}  {2:9s}'.format('No.', 'Item Description', 'Price '))
    print('\t\t\t {0:3s}  {1:26s} {2:9s}'
          .format('===', '===========================', '========='))
    for n in range(0, len(itemList)):
        print('\t\t\t {0:>2s} - {1:26s}  ${2:8.2f}'.format(str(n+1), itemList[n][0], itemList [n][1]))
    print('\n\t\t\t {0:>2s} - {1:26s} '.format('s',  'display cart contents '))
    print('\t\t\t {0:>2s} - {1:26s} '.format('x', 'return to category menu '))
    


    #The input for each menu option
    
    menuPic = input('\n\nEnter Selection (1 to {0:>2s}, "s", or "x"): '.format(str(len(itemList))))
    return menuPic          # GRS - line was missing

    
def confirmAdd(item, price, incart):   # function rewritten by GRS --------------------
    s = input('\n\t Add ' + item + ' to the cart(y/n)?: ')
    if s in 'nN':
        return incart
    if item not in cart:
        incart[item] = [1, price]
    else:
        incart[item][0] += 1
    return incart
    
    
    
    
    
def checkout (cart): 
    print(cart)
    os.system('cls')
    priceItems = 0.0
    totalItems = 0
    #print ('\n\n\t\t ' + cart + ' menu')
    print ('\n\t\t The fallowing items are your checkout cart: ')
    print('\n\t\t\t {0:26s}  {1:9s}'.format('Items selected', 'Price '))
    print('\t\t\t {0:26s} {1:9s}'
          .format('===========================', '========='))
    for c in cart:
        print('\t\t\t {0:26s}  ${1:8.2f}'.format( c, cart[c][1]* cart[c][0]))
        #totalItems += cart[c]
        priceItems += cart[c][1] * cart[c][0]
        totalItems += cart[c][0]
        
        
    print('\t\t\t {0:26s} {1:9s}'
        .format('===========================', '========='))
    print('\t\t\t {0:26s}  ${1:8.2f}'.format("total cost of items:" ,priceItems))
    print('\t\t\t {0:26s}  {1:4d}'.format("total amount of items:" ,totalItems))
    
    print("total cost of items:" ,priceItems)
    print("total amount of items:" ,totalItems)
    #print('\n\t\t\t {0:>2s} - {1:26s} '.format('s',  'display cart contents '))
    #print('\t\t\t {0:>2s} - {1:26s} '.format('x', 'return to category menu '))
        
    #while menuPic not in 's' or 'x':
        #sure = input("\n\tAdd {0:3s} to the cart (y/n)?: ".format(itemList[n]))
        #if sure == 'y':
            #print('{0:3s} was added to the cart'.format(itemList[n]))
            #break
        #else:
            #break
        #break
            

page = open('book.txt', 'r')
inlist = page.readlines()
print(page)
page.close()

book_list = []
for b in inlist:
    title,price = b.split(',')
    price = float(price)
    book_list.append([title,price])






page = open('clothing.txt', 'r')
tinlist = page.readlines()
print(page)
page.close()

clothing_list = []
for c in tinlist:
    title,price = c.split(',')
    price = float(price)
    clothing_list.append([title,price])






page = open('electronics.txt', 'r')
einlist = page.readlines()
print(page)
page.close()

electronics_list = []
for e in einlist:
    title,price = e.split(',')
    price = float(price)
    electronics_list.append([title,price])





page = open('travel.txt', 'r')
tinlist = page.readlines()
print(page)
page.close()

travel_list = []
for t in tinlist:
    title,price = t.split(',')
    price = float(price)
    travel_list.append([title,price])



valid_book_pics = [str(n + 1) for n in range(len(book_list))]   # added by GRS             
 



print("Welcome to the Amazin Store!")
numCarts = 0
totalItems = 0
priceItems = 0.0
user = 'y'
while user == 'y':
    

    

    #numCarts = 0
    #totalItems = 0
    #priceItems = 0.0
    user = 'y'
    
    cart = {} 
    subcart = {}
    #numBooks = 0
    #priceBooks = 0.0
    #numClothing = 0
    #priceClothing = 0.0
    #numElectronics = 0
    #priceElectronics = 0.0
    #numTravel = 0
    #priceTravel =0.0
    book_price = 0.0
    book_quanity = 0
    while True:
        if user == 'n':
            break
        print(""" 
       Amazin.com (22f)
         1 - Books
         2 - Clothing
         3 - Electronics
         4 - Travel
         c - Checkout
      """)
        select = input("Select '1', '2', '3', or '4' to be directed to the  department you want to shop in, or select 'c' to checkout:  ")
        while True:
                if select not in ("1", '2', '3', '4', 'c'):
                    select = input('Error!! wrong input, try again: ')
                else:
                    break
            
        if select == '1':
            while True:
                pic = itemMenu("Books", book_list)
                if pic == 'x':
                    break
                elif pic == 's':
                    print(cart)
                elif pic in valid_book_pics:           # GRS
                    name = book_list[int(pic)-1][0]
                    price = book_list[int(pic)-1][1]
                    cart = confirmAdd (name, price, cart)  # GRS
                else:
                    input(pic + ' is an invalid selection, "Enter" to continue ') #GRS
                
            
        if select == '2':
            while True:
                pic = itemMenu("Clothing", clothing_list)
                if pic == 'x':
                    break
                elif pic =='s':
                    print(cart)
                elif pic in valid_book_pics:
                    name = clothing_list[int(pic)-1][0]
                    price = clothing_list[int(pic)-1][1] 
                    cart = confirmAdd (name, price, cart)
                else:
                    input(pic + ' is an invalid selection, "Enter" to continue ') #GRS
                    
        
            
        if select == '3':
            while True:
                pic = itemMenu("Electronics", electronics_list)
                if pic == 'x':
                    break
                elif pic =='s':
                    print(cart)
                elif pic in valid_book_pics:
                    name = electronics_list[int(pic)-1][0]
                    price = electronics_list[int(pic)-1][1] 
                    cart = confirmAdd (name, price, cart)
                else:
                    input(pic + ' is an invalid selection, "Enter" to continue ') #GRS
            
            
        if select == '4':
            while True:
                pic = itemMenu("Travel", travel_list)
                if pic == 'x':
                    break
                elif pic =='s':
                    print(cart)
                elif pic in valid_book_pics:
                    name = travel_list[int(pic)-1][0]
                    price = travel_list[int(pic)-1][1] 
                    cart = confirmAdd (name, price, cart)
                else:
                    input(pic + ' is an invalid selection, "Enter" to continue ') #GRS
                    
        
        if select == 'c':
            checkout(cart)
            user = input("Are there more carts ('y,n')?: ")
            if user == 'y':
                break
            
                    
            
