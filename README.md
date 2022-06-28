# json_to_xml_convertor_momox_28_06

In this project we are trying to impliment a service which
takes input xml of employee orders and gives output as json.

Input: 
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

Output:
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

