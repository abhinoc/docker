BUCKETS

Containers for objects stored in S3

Serve several purposes:
    Organise the Amazon S3 namespace at the highest level
    Identify the account responsible for charges
    Play a role in access control
    Serve as the unit of aggregation for usage reporting


OBJECTS

Fundamental entities stored in Amazon S3

Consist of data & metadata
    Data portion is opaque to Amazon S3
    Metadata is a set of name-value pairs that describe the object
    Object is uniquely identified within a bucket by a key(name) and a version ID

KEYS

Unique identifier for a object within a bucket.
Everyobject in a bucket has exactly one key
Combination of a bucket, key & version ID uniquely identify each object.


Commands

=> List buckets
[s3-masterclass]$ aws s3 ls
2015-05-14 16:55:11 ams-iam-s3-masterclass

=> List buckets contents
[s3-masterclass]$ aws s3 ls s3://aws-ianm-s3-masterclass


=> Copy a file to an object
[s3-masterclass]$ aws s3 cp s3-masterclass-logo.txt s3://aws-ianm-s3-masterclass
upload: ./s3-masterclass-logo.txt to s3://aws-ianm-s3-masterclass/s3-masterclass-logo.txt 

[s3-masterclass]$ aws s3 ls s3://aws-ianm-s3-masterclass
2015-05-14 11:23:11     328 s3-masterclass-logo.txt



=> Stream the contents of an object to STDOUT
[s3-masterclass]$ aws s3 cp  s3://aws-ianm-s3-masterclass/s3-masterclass-logo.txt -



=> Delete an object
[s3-masterclass]$ aws s3 rm  s3://aws-ianm-s3-masterclass/s3-masterclass-logo.txt

=> Sync a directory with a bucket
[s3-masterclass]$ aws s3 sync . s3://aws-ianm-s3-masterclass
upload: ./aws_uki.txt to s3://aws-ianm-s3-masterclass/aws_uki.txt
upload: ./3-masterclass-logo.txt to s3://aws-ianm-s3-masterclass/s3-masterclass-logo.txt
upload: ./ianmmm.txt to s3://aws-ianm-s3-masterclass/ianmmm.txt


[s3-masterclass]$ aws s3 rm s3://aws-ianm-s3-masterclass --recursive
delete: s3://aws-ianm-s3-masterclass/aws_uki.txt
delete: s3://aws-ianm-s3-masterclass/s3-masterclass-logo.txt
delete: s3://aws-ianm-s3-masterclass/ianmmm.txt


=> AWS S3 CLI help
[s3-masterclass]$ aws s3 help

[s3-masterclass]$ aws s3 cp help








