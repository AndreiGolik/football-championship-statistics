import requests
from bs4 import BeautifulSoup
from config import URL, HEADERS, CHAMPIONSHIP

class ChampionshipsStaticParse:
    def __init__(self):
        self.commands = {}
        self.tables = []
        self.__clean_commands()

    def __clean_commands(self):
        self.commands = {
            "Place": [],
            "Club": [],
            "Game": [],
            "Win": [],
            "Nobody": [],
            "Lose": [],
            "Score": [],
                        }

    def __parse(self):
        response = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(response.text, "lxml")
        self.tables = soup.find_all("table", class_='tab_ligue')[:-4]
        self.__get_static()

    def __get_static(self):
        number = 0

        for table in self.tables:
            commands_static = table.find_all('tr', class_="")[1:]
            for cmd in commands_static:
                td_tags = cmd.find_all("td")
                place = td_tags[0].text

                club = cmd.find("a")
                if club is None:
                    club = td_tags[2].text
                else:
                    club = club.text

                self.commands["Place"].append(place)
                self.commands["Club"].append(club)

                digits_value = td_tags[3:11]
                for i in range(len(digits_value)):
                    value = int(digits_value[i].text)
                    self.commands[list(self.commands.keys())[i + 2]].append(str(value))

            CHAMPIONSHIP[list(CHAMPIONSHIP.keys())[number]] = self.commands
            number += 1
            self.__clean_commands()

    def run(self):
        self.__parse()
