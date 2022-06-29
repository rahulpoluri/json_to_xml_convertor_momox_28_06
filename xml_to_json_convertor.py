import xml
from typing import Dict, Union, List, Any

import xmltodict
import json
import re
import requests

ALLOWED_EXTENSIONS = ["xml"]


def placeOrder(order_json: json) -> dict:
    """places order with extracted order_json to the api"""
    try:
        headers = {}
        pload = order_json
        response = requests.post('https://URL', data=pload, headers=headers)
        if response.status_code == 200:
            return {"response_text": "Request placed successfully","response_json": order_json}
    except:
        return {"response_text": "Request is not placed","response_json": order_json}


def isaAllowedFile(filename: str) -> bool:
    """returns True if the file is .xml file """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def getDishId(dish_name: str) -> Union[str, None]:
    """returns dish list from the menu api """
    try:
        response = requests.get("http://nourish.me/api/v1/menu")
        if response.status_code == 200:
            dishes = json.loads(response.json())
            for dish in dishes:
                if dish["name"] == dish_name:
                    return dish["id"]
        else:
            return None
    except:
        return None


def getCustomerInfo(employee: dict) -> dict:
    """returns dict with customer details """
    customer, address = {}, {}
    customer_fullname = employee.get("Name")
    customer_address = employee.get('Address')
    customer_address_street = customer_address.get("Street")
    customer_address_city = customer_address.get("City")
    customer_address_pcode = customer_address.get("PostalCode")
    address["street"] = customer_address_street
    address["city"] = customer_address_city
    address["postal_code"] = customer_address_pcode
    customer["full_name"] = customer_fullname
    customer["address"] = address
    return customer


def getDishInfo(employee: dict) -> list:
    """returns dict with dish info """
    customer_dishes = employee.get("Order").split(",")
    customer_dish_list = []
    for dish in customer_dishes:
        dish = dish.split()
        dish_amount, dish_name = dish[0][0], dish[1]
        dish_id = getDishId(dish_name)
        customer_dish_list.append({"dish_id": dish_id, "amount": dish_amount})
    return customer_dish_list


def convertEmployeesInfoXmlToOrdersJson(xml_input: xml) -> json:
    """returns json formatted orders response for the employee details xml"""
    employee_orders = xmltodict.parse(xml_input, force_list={"Employee"})
    orders_list = {'orders': []}
    for employee in employee_orders.get('Employees').get("Employee"):
        if employee.get('IsAttending', False) and employee.get('Address'):
            customer_info = getCustomerInfo(employee)
            customer_dish_info = getDishInfo(employee)
            order = dict()
            order["customer"] = customer_info
            order["dishes"] = customer_dish_info
            orders_list['orders'].append(order)
    return json.dumps(orders_list)
