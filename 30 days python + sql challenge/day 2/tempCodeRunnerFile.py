
with open("users.json", 'r') as jsonfile:  
	# file should not have trailing commas
    # for trailing commas use demjson library

    data = json.load(jsonfile)
    print(data, '\n'