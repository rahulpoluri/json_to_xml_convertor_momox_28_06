import xmltodict
import json
import re
from app import get_dish_id

def convertEmployeesInfoXmlToOrdersJson(xml_file):
    # with open(r"C:\Users\WE\PycharmProjects\momoxProject\json_to_xml_convertor_momox_28_06\example_xml.xml", "rb") as xml_file:
    employee_orders = xmltodict.parse(xml_file, force_list={"Employee"})

    # create new order json
    orders_list = {'orders':[]}
    for employee in employee_orders.get('Employees').get("Employee"):
        print(employee)
        if employee.get('IsAttending', False) and employee.get('Address'):
            # extracting data for each employee
            customer_fullname = employee.get("Name")
            customer_address = employee.get('Address')
            customer_address_street = customer_address.get("Street")
            customer_address_city = customer_address.get("City")
            customer_address_pcode = customer_address.get("PostalCode")
            customer_dishes = employee.get("Order").split(",")
            customer_dish_list = []
            for dish in customer_dishes:
                dish = dish.split()
                dish_amount, dish_name = dish[0][0], dish[1]
                dish_id = get_dish_id(dish_name)
                # dish_id = 1
                customer_dish_list.append({"dish_id": dish_id, "amount": dish_amount})

            # inserting into orders
            order, customer, address = {},{},{}
            address["street"] = customer_address_street
            address["city"] = customer_address_city
            address["postal_code"] = customer_address_pcode
            customer["full_name"] = customer_fullname
            customer["address"] = address
            dishes = customer_dish_list
            order["customer"] = customer
            order["dishes"] = dishes
            orders_list['orders'].append(order)
    return orders_list










