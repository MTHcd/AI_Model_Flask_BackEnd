Classification System

Data
- Crud
-- Model1
-- Model2

- Query
-- Classification data

example:
# Create a Data source
POST website.com/api/define-model
 - name: Cars
 - attributes:
  - Color
  - Make
  - Model
  - Manufacturer
  - Year
  
POST website.com/api/define-model
 - name: Images
 - attributes:
  - Pixels[]
  - tag: "1", "Cars:F150"

# Add data to the source
POST website.com/api/model/<name>
  - <name>: Cars
  - data:
    - Color         : Blue
    - Make          : Truck
    - Model         : F150
    - Manufacturer  : Ford
    - Year          : 2016

  - return Id

# Update the data
PUT website.com/api/model/<name>/<id>
  - <name>: Cars
  - data:
    - Color         : Blue
    - Make          : Truck
    - Model         : F150
    - Manufacturer  : Ford
    - Year          : 2016

  - return Id
  
# delete the data
DELETE website.com/api/model/<name>/<id>
  - <name>: Cars
  - <id>  : 6
  - return True/False

# Query
POST website.com/api/classify
 - Name: f150
 - attribute:
  - type: Linear Regression
  - model: Cars
  - train-data: 0.8
  - test-data : 0.2

  -return id

GET website.com/api/classify/<id>?Color=<color>&...


POST website.com/api/identify
 - Name: Number
 - attribute:
  - type: Linear Regression
  - model: Numbers
  - train-data: 0.8
  - test-data : 0.2
  - tag: number

  -return id
  
GET website.com/api/identify/number?pixels=0s8s79v98asdv9a8s7d98a7sd9f8a7
  - return "{0: 0.1, 1: 0.02, 2: 0.03, 3: 0.87, 4: 0.03...}"