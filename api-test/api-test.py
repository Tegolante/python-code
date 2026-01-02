import requests

def get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'

    try:

        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def main():

    posts = get_posts()

    if posts:

        with open("api_request_get_file.txt", "w") as f:
            for post in posts :
                str(post)
                f.write(f"{post}\n")

        for post in posts :
            print('Id', post['id'])    
            print('Post Title:', post['title'])
            print('Post Body:', post['body'] + '\n')
    else:
        print('Failed to fetch posts from API.')

main()