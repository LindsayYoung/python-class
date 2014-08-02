import requests
import csv

url = raw_input("give me the capitolwords text endpoint you want to make into a spreadsheet")

response = requests.get(url).json()

with open("Reid_weekend.csv", "wb") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['speaker', 'state', 'capitolwords_url', 'speach', 'origin_url', 'title'])

	for n in response['results']:
		speaker = n['speaker_first'] + " " + n['speaker_last']
		state = n['speaker_state']
		capitolwords_url = n['capitolwords_url']
		speach = n['speaking'][0]
		origin_url = n['origin_url']
		title = n['title']
		writer.writerow([speaker, state, capitolwords_url, speach, origin_url, title])
