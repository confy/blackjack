#In order for multiprocessing to work cleanly, 
# it needs to be in a seperate file to avoid repeatedly 
# importing everything


import requests
from multiprocessing import Process

def post_request(url, data):
    """ Helper function, creates a post request """
    try:
        requests.post(url, json=data)
        return True
    except:
        return False

def post_hand(data):
        """Sends the results of the round to the hiscores"""
        p = Process(target=post_request, args=('http://localhost:5000/api/hand/', data))
        p.start()
        