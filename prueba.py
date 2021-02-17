import pymongo

myclient = pymongo.MongoClient( "mongodb://localhost:27017/")
mydb = myclient["bbdd2"]
mycol = mydb["Clientes"]

mylist = [
  { "nombre": "Manuel", "direccion": "C/ Mayor 1"},
  { "nombre": "Carlos", "direccion": "C/ Ariiba 3"},
  { "nombre": "Enrique", "direccion": "C/ Mexico 2"},
  { "nombre": "Antonio", "direccion": "C/ República Argentina"},
  { "nombre": "Javi", "direccion": "C/ Serrano 100"},
  { "nombre": "Jorge", "direccion": "C/ Diagonal 1"},
  { "nombre": "David", "direccion": "C/ Mayo 3"},
  { "nombre": "Ana", "direccion": "C/ Samaranch 14"}
]

x = mycol.insert_many(mylist)

#print lista de los valores id de los documentos insertados:
print(x.inserted_ids)