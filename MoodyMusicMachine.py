#Simple assignment
import module_manager
module_manager.review()

from selenium import webdriver 
#import string
#import pandas as pd
#import nltk

def runApp(): 
    driver = webdriver.Chrome("/Users/lauracanseco/Desktop/chromedriver")
    mood = getMood(driver)
    songs = findSongsByBPM(driver, mood)
    logIn(driver)
    setUpPlaylist(driver, mood)
    addSongToPlaylist(driver, songs)
    

def myuser():
    user = input("Logging into your Spotify... Please enter your email for Spotify: ")
    return user
    
def mypw():
    pw = input("Please enter your password: ")
    return pw

def logIn(driver):
    url = 'accounts.spotify.com'
    driver.get("https://" + url)
    driver.find_element_by_name('username').send_keys(myuser())
    driver.find_element_by_name('password').send_keys(mypw())
    driver.find_element_by_id('login-button').click()
    driver.implicitly_wait(10)
    #Opening spotify webplayer 
    driver.find_element_by_xpath("//*[@id='app']/body/div/div[2]/div/div/div[4]/div/a").click()
    driver.implicitly_wait(10)

def getMood(driver): 
    mood = input("How are you feeling today?\n")
    return mood

def setUpPlaylist(driver, mood):
    #Create a new playlist
    driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/nav/div[2]/div/div[1]/button").click()
    driver.implicitly_wait(10)
    #Set the description of the playlist 
    driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[1]/div[5]/span/button/h1").click()
    driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div[2]/div[3]/textarea").click()
    driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div[2]/div[3]/textarea").send_keys(f'My curated playlist for when I\'m feeling: {mood}!')
    driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div[2]/button").click()
    
def addSongToPlaylist(driver, songs):
    for song in songs: 
        driver.implicitly_wait(10)
        #Clicks search button
        driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/nav/ul/li[2]/a").click()
        #Clears song
        driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[1]/header/div[3]/div/div/input").clear()
        #Searches for song 
        driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[1]/header/div[3]/div/div/input").send_keys(song)
        driver.implicitly_wait(10)
        #Clicks on add playlist button
        driver.find_element_by_xpath("//*[@id='searchPage']/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/button[2]").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='context-menu-root']/ul/li[6]/button").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("/html/body/div[11]/div/ul/li[6]/div/ul/li[2]/button/span").click()
        driver.implicitly_wait(10)
    #Clicks on playlist to play 
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/nav/div[2]/div/div[3]/div[4]/div/div/ul/div/div[2]/div[1]/li/a').click()
    #Click on button to play
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[3]/div/button[1]').click()

      
'''
def moodToBPM(dataset):
    import pandas as pd
    import string
    import nltk
    
    nltk.downloader.download('vader_lexicon')

    cleanData = []
    for sentence in dataset.split(","):
        sentence = sentence.strip()
        if sentence != "":
            cleanData.append(sentence)
          
    dataset = cleanData

    ### Cited from 
    def nltk_sentiment(sentence):
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        nltk_sentiment = SentimentIntensityAnalyzer()
        score = nltk_sentiment.polarity_scores(sentence)
        return score

    ### Cited from 
    nltk_results = [nltk_sentiment(row) for row in dataset]
    results_df = pd.DataFrame(nltk_results)
    text_df = pd.DataFrame(dataset, columns = ['text'])
    nltk_df = text_df.join(results_df)

    compoundList = nltk_df["compound"].tolist()

    #print(nltk_df)
    #print(compoundList)

    averageBPM = 0
    for val in range(len(compoundList)):
        averageBPM += ((compoundList[val] * 35) + 95)
    averageBPM = int(averageBPM // len(compoundList))

    bpmRange = [i for i in range(averageBPM - 5 , averageBPM + 5)]
    print(averageBPM)
    print(bpmRange)
    return bpmRange 
'''
def findSongsByBPM(driver, mood):
    bpmRange = [112, 113, 114, 115]
    songs = []
    for num in bpmRange:
        url  = f'getsongbpm.com/tempo/{num}-bpm'
        driver.get("https://" + url)
        #Adds first song
        songs.append(driver.find_element_by_xpath('/html/body/section[2]/div[2]/div/div/div[3]/a[1]/div/div[1]/span[1]').text)
        #Adds second song
        songs.append(driver.find_element_by_xpath('/html/body/section[2]/div[2]/div/div/div[3]/a[2]/div/div[1]/span[1]').text)
    return songs

runApp()
    
    
    

    
