# Json_to_xml_convertor_momox_28_06

In this project we are trying to impliment a service which
takes input xml file of employee orders and place order in json.

Input xml format: 
```
{
	orders: [{
		customer: {
			full_name: "Max Mustermann",
			address: {
				street: "Musterweg 3",
				city: "Musterhausen",
				postal_code: "12345"
			}
		},
		dishes: [{
			dish_id: 3,
			amount: 3,
		}, ]
	}, ]
}
```

Output order json format:
```
{
	'Employees': {
		'Employee': {
			'Name': 'Max Mustermann',
			'Address': {
				'Street': 'Musterweg 3',
				'City': 'Musterhausen',
				'PostalCode': '12345'
			},
			'Order': '3x Pizza Quattro Formaggi',
			'IsAttending': 'true'
		}
	}
}
```
Note: As the endpoints are fictitious, request methods are placed in try-except block to 
handle them for failure.

