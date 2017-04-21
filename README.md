# Udacity Blog Project
## Full Stack Nano Degree
## A Google App Engine application

This is a simple blog written in Python using Google App Engine

### Accessing the demo
An online demo can be seen at [https://udacity-blog-157000.appspot.com](https://udacity-blog-157000.appspot.com/)

### Development Requirements
- Google App Engine SDK for Python [Download and install instructions](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)
- Clone this repository: `git clone https://github.com/tdbunting/multiuser_blog_ufsnd`


#### Run a development mode
- Run `dev_appserver.py .` from within the source directory
- Go to [http://localhost:8080](http://localhost:8080) in your browser
- Browse the application. Any edits to source files should reload the server automatically.

#### Deploy to an App Engine
- Create a new project on cloud.google.com
- Deploy with `appcfg.py -A [YOUR_PROJECT_ID] -V v1 update ./` where `[YOUR_PROJECT_ID]` is the project id for your new project
