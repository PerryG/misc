from pattern import web
import requests
import re

def get_log_links(p1, p2 = '', card = 'Thief', max_results = 1000):
    template = "http://gokologs.drunkensailor.org/logsearch?p1name=%s&p2name=%s&rating=pro&pcount=2&bot=false&submitted=true&supply=%s&limit=%d"
    url = template % (p1, p2, card, max_results)
    query = web.Element(requests.get(url).text)
    return [l.href for l in query.by_tag('a') if l.content == u'Log']

def get_raw_log(url):
    return web.Element(requests.get(url).text).content

def card_purchased(raw_log, player, card = 'Thief'):
    return bool(re.search('%s - buys %s' % (player, card), raw_log))

def main():
    # players = ['Stef', 'Mic Qsenoch', 'shark_bait', 'SheCantSayNo', 'awall', 'Monsieur X', 'hiroki',
    #             'Perry Green', 'Stealth Tomato', 'Java Sparrow']
    # for player in players:
    #     # print player
    #     # print filter(lambda url: card_purchased(get_raw_log(url), player), get_log_links(player))
    #     purchased_thief = map(lambda url: card_purchased(get_raw_log(url), player), get_log_links(player))
    #     info = (player, len(purchased_thief), sum(purchased_thief), float(sum(purchased_thief))/len(purchased_thief))
    #     print "Player: %s\tGames: %d\tBuys Thief: %d\tFraction: %.2f" % info
    cards = ['Governor', 'Goons', 'Chapel', 'Mountebank', 'Witch', 'Ambassador', 'Masquerade']
    player = 'impromptublue'
    for card in cards:
        buy_card = map(lambda url: card_purchased(get_raw_log(url), player, card), get_log_links(player, card = card))
        info = (card, len(buy_card), sum(buy_card), float(sum(buy_card))/len(buy_card))
        print "Card: %s\tGames: %d\tBuys: %d\tFraction %.2f" % info

main()