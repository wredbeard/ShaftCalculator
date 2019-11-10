GitHub\python\Shafts> py shaft.py


Run "python shaft.py"

Output:

```
Cylinder 1 => Dia: 5 Length: 10.25
  volume =  201.25827937059614
Cylinder 2 => Dia: 7 Length: 18
  volume =  692.7211801165494
Cylinder 3 => Dia: 4.25 Length: 7
  volume =  99.30378028456487

Overall Length: 35.25

Volume: 993.283240 cubic units

Weight: 282.092440 (lbs):
```



#Planned updates for database storage:

Shaft table schema:

```
	ID (int) Primary Key
	PartNo (string)
	Description (string)
	Material_id (int)  A lookup from Material table
	TotalWeight (Decimal)
	Price (Decimal)
	Cost (Decimal)

```
Cylinders table Schema:
```
	ID (int) Primary Key
	Shaft_id (Int) Foreign that points to a Shaft
	Diameter (Decimal)
	Length  (Decimal)
	SeqNo (int)
```

Material table schema
```
	ID (int) Primary Key
	Name (String)
	Desnsity (Decimal)
```

#-- SQL Examples:

#-- Get a Shaft, and its Material data:

```
Select * From Shafts
	Join Material on Shafts.Material_id = Material.id
	Where Shafts.ID = 12345
```
#-- Load all child cylinders for a certain shaft:

```
Select * From Cylinders Where Shaft_id = 12345
  Order By SeqNo
```


	

