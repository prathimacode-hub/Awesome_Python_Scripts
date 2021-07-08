from requests import get, exceptions
import json

def get_user_agent():
    return 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.669.0 Safari/534.20'

def get_video(url):
    try: # checks if link is valid
        r = get(
            url + '.json',
            headers = {'User-agent': get_user_agent()}
        )
    except exceptions.MissingSchema:
        print('Please provide a valid URL', 'error')
        quit()

    if 'error' in r.text:
        if r.status_code == 404:
            print('Post not found', 'error')

        quit()

    try:
        json_data = json.loads(r.text)[0]['data']['children'][0]['data']
        print('Post Found!')
        print(f'Title: {json_data["title"]}')
        print(f'In sub-reddit: {json_data["subreddit_name_prefixed"]}')
        print(f'Posted by: {json_data["author"]}')
        print('Video is successfully downloaded')
    except:
        print('Post not found')
        quit()

    try: # checks if post contains video
        video_url = json_data['secure_media']['reddit_video']['fallback_url']
        r = get(video_url).content
        with open('download.mp4', 'wb') as file:
            file.write(r)
    except TypeError:
        print('Only posts with videos are supported')

url=input('Enter Video Post Url:')
get_video(url)

#Example:
#take url='https://www.reddit.com/r/IndianGaming/comments/odcp6v/240hz_vs_60hz_gaming_monitor/'
