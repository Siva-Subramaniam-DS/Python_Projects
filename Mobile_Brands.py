class Phone:
    phone_name= "Today's Mobile"
    location= 'chrompet'
    product= 'Mobile'
    brand=set()
    brand_list=set()
    color_list=set()
    price_list=set()
    model=[]
    mobile=[]
    color=[]
    price=[]
    sort_price=[]

    def __init__(self,Mmodel,Mbrand,Mcolor,Mprice):
        self.Mmodel= Mmodel
        self.Mbrand= Mbrand
        self.Mcolor= Mcolor
        self.Mprice= Mprice
        Phone.mobile.append(self)
        Phone.brand.add(self.Mbrand)
        Phone.model.append(self)
        Phone.color.append(self)
        Phone.price.append(self)
        Phone.sort_price.append(self)
        Phone.brand_list.add(Mbrand)
        Phone.color_list.add(Mcolor)
        Phone.price_list.add(Mprice)

    #object-method to access the data
    def Mobiles_details(self):
        print (f'Mobile Model: {self.Mmodel}')
        print (f'Mobile Brand: {self.Mbrand}')
        print (f'Mobile Color: {self.Mcolor}')
        print (f'Mobile Price: {self.Mprice}')


    @classmethod
    def shop_details(cls):
        print(f'Shop Name: {cls.phone_name}
        print(f'Location: 
    product= 'Mobile'

    @classmethod
    def all_Mobiles_details(cls):
        for i in cls.mobile:
            i.Mobiles_details()
            print ('------------------------------')
    
    #class-method to display all the Brands
    @classmethod
    def Brand_Lists(cls):
         for mbrand in cls.brand:
             print(mbrand)
             print ('-----------------------------')

    #class-method to display all the Brands available in shop
    @classmethod
    def sorted_brand(cls):
        for i in cls.brand_list:
            print()
            print(f'-------------{i}-------------')
            print()
            for j in cls.mobile:
                if j.Mbrand==i:
                    j.Mobiles_details()
                    print('-------------------------------')


    #class-method to display all the Models
    @classmethod
    def Model_Lists(cls):
        for i in cls.model:
            print(f'Model Name: {i.Mmodel}')
            print ('-----------------------------')

    #class-method to display all the Colors
    @classmethod
    def color_Lists(cls):
        for i in cls.color:
            print(f'Model Color: {i.Mcolor}- Model Name: {i.Mmodel}')
            print ('-------------------------------')


    #class-method to display all the colors available in shop
    @classmethod
    def sorted_color(cls):
        print(cls.color_list)
        for i in cls.color_list:
            print()
            print(f'-------------{i}-------------')
            print()
            for j in cls.mobile:
                if j.Mcolor==i:
                    j.Mobiles_details()
                    print('-------------------------------')

    #class-method to access the Price
    @classmethod
    def price_Lists (cls):
        for i in cls.price:
            print(f'Model Price: {i.Mprice}- Model Name: {i.Mmodel}')
            print ('----------------------')

    #class-method to display all the Price available in shop
    @classmethod
    def sorted_price(cls):
        for i in cls.price_list:
            print()
            print(f'------------Rs{i}------------')
            print()
            for j in cls.mobile:
                if j.Mprice==i:
                    j.Mobiles_details()
                    print('-------------------------------')
        
    #class-method seraching base on user choice brand
    @classmethod
    def choice_brand(cls):
        brand= input('Enter your Brand Name= ')
        print(f'-------------{brand}-------------')
        if brand in cls.brand_list:
            for i in cls.mobile:
                if i.Mbrand==brand:
                    i.Mobiles_details()
                    print('-------------------------------')
        else:
            print(' ! This Brand is not Available right now ! ')

    #class-method seraching base on user choice color
    @classmethod
    def choice_color(cls):
        brand= input('Enter your color Name= ')
        print(f'-------------{brand}-------------')
        if brand in cls.color_list:
            for i in cls.mobile:
                if i.Mcolor==brand:
                    i.Mobiles_details()
                    print('-------------------------------')
        else:
            print(' ! This Brand is not Available right now ! ')
        

    #class-method seraching base on user choice price
    @classmethod
    def choice_price(cls):
        brand= int(input('Enter your price Name= '))
        print(f'-------------{brand}-------------')
        if brand in cls.price_list:
            for i in cls.mobile:
                if i.Mprice==brand:
                    i.Mobiles_details()
                    print('-------------------------------')
        else:
            print(' ! This Brand is not Available right now ! ')


c1=Phone('iphone14','Apple','black',100000)
c2=Phone('iphone15 Plus','Apple','Green',90000)
c3=Phone('redmi note 10','Xiaomi','white',15000)
c4=Phone('Techno pov 3','Techno','blue',15000)
c5=Phone('Techno Camon 20','Techno','blue',15000)
c6=Phone('realme 11x','Realme','black',15000)
c7=Phone('realme C53','Realme','gold',10000)
c8=Phone('iQOO Neo 6','iQOO','white',10000)
c9=Phone('iQOO Z6 Lite','iQOO','blue',100000)
c10=Phone('OPPO A38','OPPO','black',10000)
c11=Phone('OPPO F21','OPPO','white',90000)
c12=Phone('Galaxy S21 FE','Samsung','white',90000)
c13=Phone('Galaxy S23 Ultra','Samsung','black',100000)
c14=Phone('vivo Y78','Vivo','blue',20000)
c15=Phone('Huawei P30','Huawei','pink',90000)



        
        
