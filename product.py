#load and read csv

import csv

product_list = []


class Product:
  def __init__(self,product_name, min_age,max_age,min_salary, max_salary,risk_score):
    self.product_name = product_name
    self.min_age = min_age
    self.max_age = max_age
    self.min_salary = min_salary
    self.max_salary = max_salary
    self.risk_score = risk_score

def loadProductCsv():
 with open('product.csv') as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=',')
     line_count = 0
     for row in csv_reader:
         if line_count == 0:
             line_count += 1
         else:
           # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
             p1 = Product(row[0], row[1],row[2],row[3],row[4],row[5])
             print(p1.product_name,p1.min_age,p1.max_age,p1.min_salary,p1.max_salary,p1.risk_score)
             product_list.append(p1)
             line_count += 1
    

def getProductSuggestion(age,salary,cal_risk):
    suggested_product=[]
    for product in product_list:
      
        if int(age) >= int(product.min_age) and int(age) <= int(product.max_age):
            if float(salary) >= float(product.min_salary) and float(salary) <= float(product.max_salary):
                if int(cal_risk)-2 <= int(product.risk_score) and int(cal_risk)+2 >= int(product.risk_score):
                     suggested_product.append(product.product_name) 
    return suggested_product



loadProductCsv()
list=getProductSuggestion(20,25000,5)
for pro in list:
    print(pro)
