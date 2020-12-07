Salty Frames


Django:
django software foundation


Django REST API:
https://www.django-rest-framework.org/


Coding For Entrpreneurs:
tutorials and guides with Django.


Static Files:
I'm using Linode. The reasons:

-Store Critical Data: Object storage is the best choice for data that doesn’t change often. Store backup files, database dumps, logs, and massive data sets. All accessible over the Internet via a URL.

-High Availabilty: Linode Object Storage is highly available and durable. Objects are replicated across servers so they’re always accessible even if one of the servers goes offline.

-Linode is available for ($0.02/GB) as opposed to Google Cloud's ($.02/GB) and AWS's ($.022/GB). As a matter of fact, I used to use AWS S3 but was being charged too much.

You may use your own computing cloud architecture. You would then use saltyframes/settings/base.py and modify or delete the following code.:
code here.



