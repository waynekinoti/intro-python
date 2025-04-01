
data = {
    "name": "Jackie Wang",
    "dob":"2007-2-3",
    "email":"wang@gmail.com",
    "school":{
        "name":"MFA",
        "county":"Nakuru",
        "ksce":{
            "score": "A",
            "students":268
        }


    }

}

print(data["dob"])
county = data["school"]["county"]
print(county)
print(data["school"]["kcse"]["score"])