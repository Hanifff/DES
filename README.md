# Data Encryption Standard (DES) and TripleDES

## Requirements packages 
In order to run the scripts, the last python version (3.7.x) is required.<br>

Flask need to be installed<br>
https://flask.palletsprojects.com/en/1.1.x/installation/<br>

Other pacakges that need to be installed:<br>
pip install multiprocess<br>
pip install more-itertools<br>
pip install joblib<br>
pip install functools<br>
pip install pyoperators<br>

## File structures and Running the code
### DES:
An implementation of a simplified version of DES algorithm (SDES) which is able to crack binary ciphered texts.<br>


### TrippleDES:
An implementation of a simplified version of a tripple DES algorithm (SDES) which is able to crack binary ciphered texts.<br>

### A simple webserver:
Theres is also a webserver that run on localhost and tests the application. 

## Run the apllication:
Use the command:<br>
`main.py`

Run the webserver:<br>
`flask run`

The results of tests will be uploaded to the results folder, which contains the answer to decryption/encryption tasks.<br>
The cipher folder contains ciphertext files.<br>
The static directory contains the HTML and javascript file for the front-end part of the website.<br>
