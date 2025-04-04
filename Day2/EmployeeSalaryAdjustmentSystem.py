employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]
def salary(employee):
    if employee['rating'] == 4 or employee['rating'] == 5:
        employee['salary'] =employee['salary']* 1.10 
    elif employee['rating'] == 3:
        employee['salary'] =employee['salary']* 1.05  
    elif employee['rating'] == 1 or employee['rating'] == 2:
        employee['salary'] =employee['salary']* 0.97 

    return employee


upadated_result=list(map(lambda emp:salary(emp), employees))
print(upadated_result)
