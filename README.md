# Json_to_xml_convertor_momox_28_06

In this project we are trying to impliment a service which
takes input xml file of employee orders and place order in json.

Input xml format: 
```
?xml version="1.0" encoding="utf-8"?> 
<Employees>
	 <Employee>
		 <Name>Max Mustermann</Name>
		 <Address>
			 <Street>Musterweg 3</Street>
			 <City>Musterhausen</City>
			 <PostalCode>12345</PostalCode>
		 </Address>
		 <Order>3x Pizza Quattro Formaggi</Order>
		 <IsAttending>true</IsAttending>
	 </Employee>
 ...
</Employees>
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

