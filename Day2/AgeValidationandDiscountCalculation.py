customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]


def age_validation(customer):

    if customer["age"]>=18 and customer["age"]<=25:
        customer["total_purchase"]=customer["total_purchase"]*1.10
    elif customer["age"]>=26 and customer["age"]<=40:
        customer["total_purchase"]=customer["total_purchase"]*1.05


    return customer


eligible_customers = filter(lambda cust: 18 <= cust["age"] <= 40, customers)


updated_results = list(map(age_validation, eligible_customers))


print(updated_results)



        
