"# MuddHacks2018" 

Arduino camera module takes a picture, then sends it over to a locally run TensorFlow model via Flask. The model is used to analyze the image, return an identification of all the objects in frame, and sends back the data via Flash once more. A speaker module on the Arduino reads aloud the objects in frame for the user.
