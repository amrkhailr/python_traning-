#8. Software Sales
#A software company sells a package that retails for $99. Quantity discounts are given
#according to the following table:
#Quantity Discount
#10–19 20%
#20–49 30%
#50–99 40%
#100 or more 50%
#Write a program that asks the user to enter the number of packages purchased. The program should then display the amount of the discount (if any) and the total amount of the
#purchase after the discount.

User = int(input('Enter the number of packages you purchased '))

retail_price = 99
discount1 = 99*0.2
discount2 = 99*0.3
discount3 = 99*.04
discount4 = 99*0.5

total_purchase1 =  (User*retail_price) - discount1
total_purchase2 =  (User*retail_price) - discount2
total_purchase3 =  (User*retail_price) - discount3
total_purchase4 =  (User*retail_price) - discount4
if User <= 1 and User <= 9:
    print('You are not qualified for the discount')
elif User >= 10 and User <= 19 :
    print('Your total discount is',discount1,'and your total purchase after discount is',total_purchase1 )
elif User >= 20 and User <= 49:
    print('Your total discount is',discount2,'and your total purchase after discount is',total_purchase2 )
elif User >= 50 and User <= 99:
    print('Your total discount is',discount3,'and your total purchase after discount is',total_purchase3 )
elif User >= 100 :
    print('Your total discount is',discount4,'and your total purchase after discount is ' '$',total_purchase4)





    