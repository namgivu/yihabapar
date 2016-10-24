#!/usr/bin/python
'''
Clone an external git repository to sub folder inside another git repo
'''


def download_from_s3(bucket, filename, saveTo, s3Key, s3Secret):
  #connect bucket
  import boto
  conn = boto.connect_s3(s3Key, s3Secret)
  b = conn.get_bucket(bucket)

  #get bucket key form filename
  key = b.get_key(filename)

  #download
  key.get_contents_to_filename(saveTo)

