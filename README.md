# Mom's Kitchen, the waste reduction network

There are three applications to our project. 

## WEBSITE

### Installing
```
python
django
docker
```
### Prerequisites

```
django
firebase-admin
pyrebase
google-cloud-firestore
channels
python 3
requests
```

### How to install the prerequisites

First download python 3 from the website.
Once you downloaded python you must install pip.
To do so run the following commands in your favourite terminal bash or cmd :
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

To launch the project and download the prerequisties the best solution is to work in a virtual environment.
First download virtualenv using the command : pip install virtualenv
Once you have downloaded it, create your environment.
Go to the source of the project.
Run the following command :
```bash
virtualenv virtual
virtual\Scripts\activate
```
Once you are in your environment you can install the dependencies.
To do so just run : pip install -r requirements.txt
Wait and congrats your dependencies were successfully installed.
You can now run manage.py.

### Deployment

```
python3 manage.py runserver
docker run -p 6379:6379 -d redis:2.8
```
### Built With
* [Django](https://www.djangoproject.com) - Python Framework
* [Docker](https://www.docker.com) - virtualisation
* [Redis](https://redis.io) - in-memory data structure project
* [Firebase](https://firebase.google.com) - database

## ANDROID
The Android project must be launched with Android Studio running a virtual Android machine

The Android tool is running an API of level 28. It contains six views : one for the login, the signup, the community tab, the homepage, the messenger and the profile.
It is coded in Kotlin and uses XML to markup the interface.
It is using a black interface in order to reduce the consumption of energy.
It is using Firebase as a database and server for accounts.

## IOS
The iOS project must be launched on a Mac with Xcode Studio. Moreover, it needs Cocoapods installed and Firebase installed too : https://firebase.google.com/docs/ios/setup
