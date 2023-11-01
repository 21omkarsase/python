import json

# Reading JSON file
# JSON file data to python list of dictionaries

print("Reading JSON file\n")

with open("files/users.json", 'r') as jsonfile:  
	# file should not have trailing commas
    # for trailing commas use demjson library

    data = json.load(jsonfile)
    print(data, '\n')

# JSON string to python list of dictionaries

json_string = '[{"login": "mojombo", "id": 1, "node_id": "MDQ6VXNlcjE="},{"login": "defunkt", "id": 2, "node_id": "MDQ6VXNlcjI="},{"login": "pjhyett", "id": 3, "node_id": "MDQ6VXNlcjM="}]'
data = json.loads(json_string)
print(data, '\n')

# writing in json file
print("Writing in JSON file\n")

data = [{"login": "mojombo", "id": 1, "node_id": "MDQ6VXNlcjE="},{"login": "defunkt", "id": 2, "node_id": "MDQ6VXNlcjI="},{"login": "pjhyett", "id": 3, "node_id": "MDQ6VXNlcjM="}]
# data = {'name': 'John Doe', 'age': 30, 'city': 'New York'}

# Converting dictionary / list of dictionaries to JSON file
with open('files/user_output.json', 'w') as jsonfile:
	json.dump(data, jsonfile)

# Converting JSON to JSON string
json_string = json.dumps(data, indent = 2)
print(json_string, '\n')
print(type(json_string)) # str

# for pretty writing / printing use -> indent = some number

# for file containing json with sorted keys
# json.dump(data, jsonfile, sort_keys=True)
