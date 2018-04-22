import requests
import json

OAuthToken = 'BQC2iZEQfuumTPZa-hBzax4qZOVlLHJMgR4SwVBhylOZGH33SqFJV0tsbApWaEoSRsm8KveXa0EvWQD-9AmNU3mOfj1OlXJ9xEuCgSPWaGEBd00kjhZdwFC4MHsD1FIcR92gxJsz5-wBhekQzteMaJzF4yF1aEqyAhGPfqkluiSKxjozOHLZrtvoKmE4wa0UJtUIv4q6KpmV4d8GKqNB2Y5rWYE_b4PjEuGCImG9BYOteWqJmK3XhUYlBNYhNMnDLDRmGCntg0PqGMg'

playlist_list = [
    ['fanmusictop2016', '086GZ4HCxg4VxGjLi0dLXs'],
    ['1276640268', '2Ct11iXczMd4Z4ejZGYWUN'],
    ['dinosudbrack', '7sYAbrWf1c6bBuihDW4Nqx']]

with open("output.csv", 'w') as fh:
    fh.write("id,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature\n")    

    for playlist in playlist_list:
        track_ids = []

        content = requests.get("https://api.spotify.com/v1/users/{}/playlists/{}/tracks".format(playlist[0], playlist[1]),
                    headers={"Accept" : "application/json",
                             "Content-Type" : "application/json",
                             "Authorization" : "Bearer {}".format(OAuthToken)}).text

        output = json.loads(content)

        for i in output['items']:
            track_ids.append(i['track']['id'])

        suffix = track_ids[0]
        for i in range(1, len(track_ids)):
            suffix += ",{}".format(track_ids[i])
        
        url = "https://api.spotify.com/v1/audio-features?ids={}".format(suffix)

        content = requests.get(url,
                    headers={"Accept" : "application/json",
                             "Content-Type" : "application/json",
                             "Authorization" : "Bearer {}".format(OAuthToken)}).text

        output = json.loads(content)
    
        for a in output['audio_features']:
            fh.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                a['id'],
                a['danceability'],
                a['energy'],
                a['key'],
                a['loudness'],
                a['mode'],
                a['speechiness'],
                a['acousticness'],
                a['instrumentalness'],
                a['liveness'],
                a['valence'],
                a['tempo'],
                a['duration_ms'],
                a['time_signature']))
    
