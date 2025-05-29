import requests, random, json

def main():
    id = random.randint(1, 100)
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    response = requests.get(url)
    obj = response.json() 
    print("userId: ",obj['userId']) 
    print("title: ",obj['title'])
    print("body: ",obj['body'])
    print("id: ",obj['id'])

if __name__ == "__main__":
    main()