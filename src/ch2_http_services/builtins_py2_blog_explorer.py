import datetime
import collections

import sys

Post = collections.namedtuple("Post", 'id title content published view_count')

base_url = 'http://consumer_services_api.talkpython.fm/'


def main():
    print "Blog explorer (Python 2 builtins version)"
    if sys.version_info.major != 2:
        print "This sample requires Python 2 (old school urllib2), exiting..."
        return

    while True:
        action = raw_input('What to do with this blog api? [l]ist, [a]dd, [u]pdate, [d]elete, e[x]it: ')
        if action == 'x':
            print "Exiting..."
            break
        if action == 'l':
            posts = get_posts()
            show_posts(posts)
        if action == 'a':
            add_post()
        if action == 'u':
            update_post()
        if action == 'd':
            delete_post()


def show_posts(posts):
    if not posts:
        print "Sorry, no posts to show."
        return

    print "------------------------------ BLOG POSTS -----------------------------------"
    max_width = max((len('{:,}'.format(int(p.view_count))) for p in posts))
    for idx, p in enumerate(posts):
        padded = ' ' * (max_width - len('{:,}'.format(int(p.view_count))))
        print "{}. {} [{}{:,}]: {}".format(idx + 1, p.id, padded, int(p.view_count), p.title)
    print


def get_posts():
    url = base_url + 'api/blog'
    resp = None  # ????

    if resp.status_code != 200:
        print "Error downloading posts: {} {}".format(resp.status_code, resp.text)

    return [
        Post(**post)
        for post in resp.json()
        ]


def add_post():
    now = datetime.datetime.now()
    published_text = '{}-{}-{}'.format(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

    title = raw_input('title: ')
    content = raw_input('content: ')
    view_count = int(raw_input('view count: '))

    post_data = dict(title=title, content=content, view_count=view_count, published=published_text)
    url = base_url + 'api/blog'
    headers = {'content-type': 'application/json'}

    resp = None  # ????

    if resp.status_code != 201:
        print "Error creating post: {} {}".format(resp.status_code, resp.text)
        return

    post = None  # ????
    print "Created this: "
    print post


def update_post():
    print("THIS METHOD DOES NOT WORK WITH URLLIB 2")
    print("You can only specify GET or POST, this method requires PUT")
    print


def delete_post():
    print("THIS METHOD DOES NOT WORK WITH URLLIB 2")
    print("You can only specify GET or POST, this method requires DELETE")
    print


if __name__ == '__main__':
    main()
