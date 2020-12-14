<h1 align="center">Salty Frames</h1>
<p align="center">
    <img src="https://img.shields.io/github/issues/RayGar7/SaltyFramesAPI" alt="Build">
</p
>
<p align="center">
    <a href="#overview">Overview</a>
    <a href="#installation">Installation</a>
    <a href="#usage">Usage</a>
    <a href="#issues">Issues</a>
    <a href="#license">License</a>
    <a href="#license">Acknowledgements</a>
</p>

<h2 align="center">Overview</h2>
<hr>
<p>Salty Frames is a fighting game frame data application. While there are many applications of these kind in the market, my implementation is designed to be pragmatic in the sense that updates to the data are as automated as possible. From my experience, other developers and myself included have struggled with data changing very oftenly and when we're dealing with frame data we're dealing with many entries per character so it is not feasible for a single developer to update data manually on his or her own. One solution is to collect the data with an automation tool. For instance, my frame data for Soulcalibur is pulled from 8 Way Run - a wiki where approved users can enter frame data. (I have received permission to do this with the condition that I save the data into my own database which I have). That is what I mean by collecting the data. This is a common procedure for data mining projects. Every time the data changes, which I can tell by saving a timestamp into my models for each character, I re-collect the data. <br> Salty Frames also provides an API for other users to create their own frame data apps. From my experience the community that likes these kind of video games has a lot of developers and they all have their own frameworks, tools and takes on the frame data genre. Only one other developer who I've known before making this project. The API is provided thanks to the Django Rest Framework or DRF. That is why you can see the generic views on some of the API endpoints made by the DRF.
</p>


<h2 align="center">Installation</h2>
<hr>
Create a virtual environment of your choice. <br>In that virtual environment run

```
pip install -r requirements.txt
```

<br>This will install all of the requirements that I installed to bring this app to its current state. <br><br>Next, as a typical Django project run:

```
python manage.py migrate
```

```
python manage.py runserver
```

```
python manage.py createsuperuser
```

Enter your desired super user details and you're up to speed.



<h2 align="center">Usage</h2>
<hr>
<p>

</p>


<h2 align="center">Issues</h2>
<hr>
<p>

</p>

<h2 align="center">License</h2>
<hr>
<p>

</p>

<h2 align="center">Acknowledgements</h2>
<hr>
<p>There are several people I have to thank for making this possible.<br><br>Coding for Entrpreneurs - a virtual academy centered around Django projects. I learned Django, the Django Rest Framework, Linode, Heroku and other tools with his tutorial series's.<br><br>8 Way Run - an online wiki for Soulcalibur. They have editors providing frame data for every Soulcalibur game. I was given permission by them to use their data with the condition that I save the data that I use into my own database. <br><br>Bandai Namco and Project Soul - they are the publisher and developer respectively for Soulcalibur VI. I'm very passionate for this video game and wanted to create a programming project with this game as a topic.</p>

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

You may use your own computing cloud architecture. You would then use saltyframes/settings/base.py and modify or delete the following code. If you also want to use
Linode (which I highly recommend) then you would set these environment variables on your .env file:



