# Image DB in Flask 
> It's a Image data base made in Flask.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Ideas for Improvements](#ideas-for-improvements)
* [Contact](#contact)


## General Information
- A API that able to store image files by http protocol and can download storaged image as well.
- This API was created to make easy to store a bunch of images files.
- The mainly reason that inspired to make this project was to be able to store any image files and can download them as zip file lately.
- This API was created to pratice my skills.



## Technologies Used
- Python - version 3
- Flask - version 2.0


## Features
Features:
- Protection to just store jpg, png and gif files.
- See what images are stored on DB.
- Can download as zip file any image or all specific type of images.


## Setup
If you want to change something to your necessties, feel free to fork or clone the project and use the requirements.txt file to install required dependencies.

These dependencies are mainly:

pip
environs
Jinja2
pytest (to test the code)
werkzeug

## Usage

### End-Points

#### GET

> `/files`


> `/files/<string:type>`

- This end-point serves you a a bunch of specific type of images.
- You'll need to specify by type you want. It can be jpg, png and gif.

> `/download/<string:file_name>`

- This end-point serves you a specific image by its name.


> `/download-zip`

- The `/download-zip` has a query params that you tell how you can download the zip file.
- The first argument is: `file_type`, it is a string argment type. With this you can choose by "png", "jpg" or "gif" to download all that files type on the DB as zip.
- The second one is: `compression_rate`. With this your telling which compression ou wanna compress your zip file.
- These arguments are *indispensable* to the end-poit works!

#### POST

> `/upload`

- It just allows images less than 1MB. 



## Project Status
Project is: _in progress_


## Ideas for Improvements
In the future extend more this project, to be a largest API with goods features to store any type of file and any size.



## Contact
Created by [@Hender-hs](https://github.com/Hender-hs). My own Portifolio Web Site [here](https://portifolio-p.vercel.app/)  - feel free to contact me!
