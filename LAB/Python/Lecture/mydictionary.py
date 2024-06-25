#Python dictionary is also called JSON in other programming languages
#JavaScript Object Notation (JSON)
#Dictionary also using the curly bracket {}
#The data id ordered
#The data is indexed by key not by number
#Every single data is associated with key
#For example firstname is a key and Peter is the data
#key cannot be duplicated, data can
#it's modifiable


foreigner = {
    "firstname":"Peter",
    "lastname" : "parker",
    "passportnumber" : "E4837589",
    "incometaxnumber": "SG834934",
    "pcbamount": 892,
    "lastmonth":5,
    "lastyear": 2024,
    "previousmonth":[(4,2024,891), (3,2024,895), (2,2024,893), (1,2024,892)],

    "addresses":{
        "office":{
            "street":"15, Lorong 8/10",
            "taman":"Puchong"
            
        },
        "home": {
            "street": "N0 48, Jalan 4/4",
            "taman": "Subang",
        }
    },
    "contact": "0169231729"
}

print("First Name:", foreigner ["firstname"])

print("transaction:", "Month", "Year", "Amount")
for month, year, amount in foreigner ["previousmonth"]:
    print(f"Transaction:, {month} - {year}, RM{amount}")

officeAddress = foreigner["addresses"]["office"]
print("Street:", officeAddress["street"])
print("Taman:", officeAddress["taman"])

homeAddress = foreigner["addresses"]["home"]
print("Street:", homeAddress["street"])
print("Taman:", homeAddress["taman"])

#you can access the street directly as follows
foreigner["addresses"]["office"]["street"]

#sometimes we dont know the ket, we can use method .key

print() #TOO SLEEPY AND TIRED GO WATCH VIDEO TO KNOW THE REST OF THE CODE (24TH JUNE)