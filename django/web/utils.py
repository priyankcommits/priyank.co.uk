import boto3
import csv


def get_bucket():
    c = boto3.resource('s3')
    bucket = c.Bucket('priyank.co.uk')
    return bucket


def get_post_likes():
    bucket = get_bucket()
    bucket.download_file('likes.csv', '/tmp/likes.csv')
    likes_dict = {}
    with open('/tmp/likes.csv', "r") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            likes_dict[row[0]] = row[1]
    return likes_dict


def post_like(post_id, count):
    bucket = get_bucket()
    bucket.download_file('likes.csv', '/tmp/likes.csv')
    with open('/tmp/likes.csv', "a", newline='') as csvfile:
        data = csv.writer(csvfile, delimiter=',')
        data.writerow([post_id, count])
    bucket.upload_file('/tmp/likes.csv', 'likes.csv')


def create_subscriber(name, email):
    bucket = get_bucket()
    bucket.download_file('subscribers.csv', '/tmp/subscribers.csv')
    with open('/tmp/subscribers.csv', "a", newline='') as csvfile:
        data = csv.writer(csvfile, delimiter=',')
        data.writerow([name, email])
    bucket.upload_file('/tmp/subscribers.csv', 'subscribers.csv')
