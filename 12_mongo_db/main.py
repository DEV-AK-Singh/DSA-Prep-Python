import bson.json_util
import pymongo as pm 
import bson

myclient = pm.MongoClient("mongodb+srv://abhishek:singh1510abhishek@healthcareerp.rza19p2.mongodb.net/", tlsAllowInvalidCertificates=True)
mydb = myclient["test"]

def get_all_users():
    mycol = mydb["users"]
    users = []
    for x in mycol.find():
        users.append(x)
    return users

def save_user_to_json(users):     
    try:
        with open("users.json", "w") as f:
            f.write(bson.json_util.dumps(users))
    except Exception as e:
        print(e)

def create_collection(collection_name):
    mycol = mydb[collection_name]
    x = mycol.insert_one({"name": "John", "address": "Highway 37"})
    print(x.inserted_id)
    print(mycol.find_one())

def delete_collection(collection_name):
    mycol = mydb[collection_name]
    mycol.delete_many({})

def update_collection(collection_name):
    mycol = mydb[collection_name]
    mycol.update_one({"name": "John"}, {"$set": {"address": "Canyon 123"}})    

def main():
    # users = get_all_users()
    # save_user_to_json(users)
    create_collection("users_x")
    # delete_collection("users_x")
    update_collection("users_x")

if __name__ == "__main__": 
    main()            