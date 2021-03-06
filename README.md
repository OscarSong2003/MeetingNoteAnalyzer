# Audio/Meeting Notes Analyzer


- A simple interface that allows the user to record one/multiple voices
- Uses Django as backend framework, and Forte to conduct processing. Also uses google speech to text recognition API to transcribe text. 
- Conducts speaker segmentation to identify speakers. 
- Uses Stave to display the annotations 
- Front end is built using React, React-Bootstrap, React-voice-recording library, and Chokra UI

# To Start:
- Clone Repository 
- Set up virtual environment: https://virtualenv.pypa.io/en/latest/user_guide.html (Command: virtualenv venv p=python3.8.5)
   NOTE: make sure to specify python version
- Navigate to frontend and pip install libraries specified in requirements.txt 
- Navigate into backend and npm install packages from package.json
- In frontend directory: run npm run start to start server on localhost:3000
- In backend directory: run python manage.py runserver to start backend 

# Restrictions
- Currently the analysis cannot handle very large/long audio files as it would require the use of cloud storage and asynchronous requests (user can implement this on top of current implementation if necessary) 
- Feel free to checkout the branch google-api-method if you wish to use your own api key (currently uses default generated by python library. 
- Additional optimizations can be made on recognition and NER. 

# Analysis Tools Used
- forte pipelines for NER and audio processing: https://github.com/asyml/forte
- pydub and google speech api: https://github.com/jiaaro/pydub
- stave for front-end annotations: https://github.com/asyml/stave 

# Video Demonstration (Informative Purpose Only)
- https://drive.google.com/file/d/1m-qdOyXkY3p4a4CR-P371-vU2ZP0eGBe/view?usp=sharing

# File Locations
- notes/media/documents contains both audio processing and processing (files for speaker segmentation and speech recognition)
- notes/media/nameEntityRec contains file for NER and running the forte pipeline and stave processor
- notes/ contains files for django (views.py consists of rest framework) 
- frontend/components contains recording component along with basic page components. 
- frontend/ also ctontains react basic setup and chokra setup 
