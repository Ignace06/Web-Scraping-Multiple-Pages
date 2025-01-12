import streamlit as st

import pandas as pd
import numpy as np

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import sys
sys.path.insert(1, '../Src/Lib')
from config import *

from Recommender import recommender

import pickle
import yaml

def main ():
	
	options = ["Main", "Stop"]
	choice = st.sidebar.selectbox("Menu", options, key = "1")
	if (choice == "Main"):
		col1, col2 = st.columns(2)
		col1.title("Spot-me-songs")
		col1.write("By Alfonso Muñoz and Ignace Gravereaux, 2022")
		col2.image("../Images/Spot-me-songs200.png")
		st.header("Get song recommendations from a database with more than 3500 songs!")
		song = st.text_input("Title of your song:")
		if song:
			def search_song(song):
	
				sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= Client_ID, client_secret= Client_Secret))
				results = sp.search(q=song, limit = 5)
			
				st.write("Pick the one you meant:")
    
				for track in results["tracks"]["items"]:
					selection = st.button("{} by {} from {}".format(track["name"], track["artists"][0]["name"], track["album"]["name"]))
					url = track["external_urls"]["spotify"]
					url2 = url.split("m/t")
					embed = url2[0]+"m/embed/t"+url2[1]
					spotify = '<iframe style="border-radius:12px" src={} width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'.format(embed)
					st.markdown(spotify, unsafe_allow_html=True)
					
					if selection:
						recommender(track)
					
				st.write("If it is not there, try again!")

			search_song(song)
			
	else:
		st.stop()
    
main()