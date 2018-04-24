# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Movie(Video):
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    """This class provides a way to store movie related information"""
	
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
    	self.title = movie_title
    	self.storyline = movie_storyline
    	self.poster_image_url = poster_image
    	self.trailer_youtube_url = trailer_youtube
        # initialize instance of class Movie

class Tvshow(Video):
    def __init__(self, season, episode, tv_station):
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
        
    def show_trailer(self):
    	webbrowser.open(self.trailer_youtube_url)
