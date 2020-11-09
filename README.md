
Moody Music Machine
(by Team LJS: Laura, Jeremiah, Stephanie)
Description
Our project generates a Spotify playlist based on the user’s mood. We run natural language sentiment analysis (using NLTK) on the user’s given mood and convert the input to beats per minute. The program then finds songs within a range of that BPM. Finally, it generates a playlist of twenty songs directly in the Spotify account (using Selenium). 
Visuals
Screen Recording of Demo- https://drive.google.com/drive/folders/1cqu7yJRmBqDVTJhNi3UivDTaqQit26YO?usp=sharing  
Modules
This project uses several modules in Python, namely:
	•	Selenium  
	•	Pandas 
	•	NLTK 
	•	String 

Usage
Run the file “moodyMusicMachine.py”. The user will need to answer a question about their current mood. The program will also ask the user for their Spotify information so that Selenium can log into the user’s Spotify account and create a playlist for the user.
Next Steps
Support for genre, artist and popularity filters for more curative playlists 
Encryption for user information ie Spotify Username and Password
A more robust implementation of sentiment analysis by lexicon
