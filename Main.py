import requests
import telegram
import time

Token = 9158978653:AAFmbP2sidlBmmG_9Bj20aS8qS8v4uC8Zro
CHAT_ID = 637202568
API_KEY = 976dffef65a08356964e24722c980bb0

bot = telegram.Bot(token=TOKEN)

TEAMS = [
  85,  #PSG
  541, #Real Madrid
  529, #Barcelone
  42,  #Arsenal
  2384, #France
  2382, #Belgique

]

know_matches = set()
while True:

    try:

        response = requests.get(

            "https://v3.football.api-sports.io/fixtures?next=50",

            headers={"x-apisports-key": API_KEY}

        )

        data = response.json()

        for match in data["response"]:

            fixture_id = match["fixture"]["id"]

            if fixture_id in known_matches:

                continue

            home_id = match["teams"]["home"]["id"]

            away_id = match["teams"]["away"]["id"]

            if home_id in TEAMS or away_id in TEAMS:

                home = match["teams"]["home"]["name"]

                away = match["teams"]["away"]["name"]

                date = match["fixture"]["date"]

                bot.send_message(

                    chat_id=CHAT_ID,

                    text=f"⚽ Match à venir\n\n{home} vs {away}\n📅 {date}"

                )

                known_matches.add(fixture_id)

        time.sleep(3600)

    except Exception as e:

        print(e)

        time.sleep(300)

