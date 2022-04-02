import requests
from bs4 import BeautifulSoup

class Webscrape():
    
    def __init__(self):
        self.unrated = {
            'Not Rated',
            'Unrated',
        }

    # year, imdb rating, intended audience, runtime
    def get_info(self, imdb_num):
        url = f'https://www.imdb.com/title/tt{imdb_num}/'
        page = requests.get(url) # Replace with other imdb link
        soup = BeautifulSoup(page.content, 'html.parser')

        li = [x.get_text() for x in soup.find_all(class_='ipc-inline-list__item')]
        x = 0
        while not li[x][-4:].isnumeric():
            x += 1
        # shift = -1 if li[2][-1].isnumeric() else 0 # some movies don't have trivia
        has_audience = 1 if not li[x+1][0].isnumeric() else 0 # some movies don't have an "Unrated" option...
        '''
        0 Cast & crew
        1 User reviews
        2 Trivia
        3 Episode aired Apr 6, 1997
        4 PGPG
        5 1h 47m
        '''
        # print(li[:6])
        # print(f'date: {x}', f'missing_audience: {has_audience}')
        year = li[x][-4:]
        if has_audience: audience = li[x+1][:len(li[x+1])//2]
        else: audience = audience = 'Unrated'
        runtime = self.string_to_minutes(li[has_audience + x + 1])

        imdb_rating = soup.find_all(class_='sc-7ab21ed2-1 jGRxWM')[0].get_text() # rating from imdb
        
        # print(year, imdb_rating, audience, runtime)
        return year, imdb_rating, self.unrated_helper(audience), runtime

    def string_to_minutes(self, timestring):
        # 1h 48m
        # 2h 03,
        hours_mins = timestring.strip().split()
        if (len(hours_mins) == 2) : return int(hours_mins[0][-2]) * 60 + int(hours_mins[1][-3:-1])
        if (hours_mins[0][-1] == 'm'): return int(hours_mins[0][:-1]) # if only minutes runtime
        return int(hours_mins[0][-2]) * 60

    def unrated_helper(self, s):
        if s in self.unrated:
            return 'Unrated'
        return s

'''
check
'''
if __name__ == '__main__':
    li = [
        '0114117', # 1997 7.6 Unrated 107
        # '0112896', # 1995 5.8 Unrated 88
        # '0114709', # 1995 8.3 Unrated 81
        # '0114916', # 1995 6.6 Unrated 94
        # '0114814', # 1995 8.5 Unrated 106
        # '0113819', # 1995 7.0 Unrated 95
        # '0114916', # 1995 6.6 Unrated 94
        # '0110299', # 1994 7.5 Unrated 116
        # '0113247', # 1995 8.1 Unrated 98
        # '0113283', # 1995 6.6 Unrated 106
        # '0106473', # 1992 7.6 TV-14 93
        '0109890',
        '0109891',
        '114709',
    ] # problems


    scraper = Webscrape()
    for x in li:
        scraper.get_info(x)
        print()

