# Python import
from datetime import date
from random import randint
# Local import
from players.models import Team, League, Player, PlayerStatusChoice, PlayerDominantLegChoice, PlayerPositionChoice


def create_test_leagues():
    League.objects.get_or_create(name='Premier League')
    League.objects.get_or_create(name='MLS')
    League.objects.get_or_create(name='UEFA Champions League')
    League.objects.get_or_create(name='Bundesliga')
    League.objects.get_or_create(name='English Football League')
    League.objects.get_or_create(name='France Ligue 1')
    League.objects.get_or_create(name='Serie A')
    League.objects.get_or_create(name='UEFA Europa League')
    League.objects.get_or_create(name='FIFA')
    return League.objects.all()


def create_test_teams():
    Team.objects.get_or_create(name='Chelsea F.C.', country='United Kingdom', city='London')
    Team.objects.get_or_create(name='FC Barcelona', country='Spain', city='Barcelona')
    Team.objects.get_or_create(name='Liverpool F.C.', country='United Kingdom', city='Liverpool')
    Team.objects.get_or_create(name='Manchester City F.C.', country='United Kingdom', city='Manchester')
    Team.objects.get_or_create(name='Manchester United F.C.', country='United Kingdom', city='Manchester')
    Team.objects.get_or_create(name='Arsenal F.C.', country='United Kingdom', city='London')
    Team.objects.get_or_create(name='Tottenham Hotspur F.C.', country='United Kingdom', city='London')
    Team.objects.get_or_create(name='Real Madrid C.F.', country='Spain', city='Madrid')
    Team.objects.get_or_create(name='FC Bayern Munich', country='Germany', city='Munich')
    return Team.objects.all()


def __get_test_players_names():
    return ['Jan', 'Stanisław', 'Andrzej', 'Józef', 'Tadeusz', 'Jerzy', 'Zbigniew', 'Tomasz',
            'Krzysztof', 'Henryk','Ryszard', 'Kazimierz', 'Marek', 'Marian', 'Piotr', 'Eugeniusz'
            'Janusz', 'Władysław', 'Adam', 'Wiesław', 'Zdzisław', 'Edward', 'Mieczysław',
            'Roman', 'Mirosław', 'Grzegorz', 'Czesław', 'Dariusz', 'Wojciech', 'Jacek']


def __get_test_players_surnames():
    return ['Nowak', 'Kowalska', 'Wiśniewska', 'Wójcik', 'Kowalczyk', 'Kamińska', 'Lewandowska',
            'Zielińska', 'Szymańska', 'Woźniak', 'Dąbrowska', 'Kozłowska', 'Jankowska',
            'Wojciechowska', 'Kwiatkowska', 'Mazur', 'Krawczyk', 'Kaczmarek', 'Piotrowska',
            'Grabowska', 'Pawłowska', 'Michalska', 'Zając', 'Król', 'Jabłońska',
            'Wieczorek', 'Nowakowska', 'Wróbel', 'Majewska', 'Stępień']


def __get_test_players_countries_with_cities():
    return [('Algieria', 'Algier'), ('Etiopia', 'Addis Abeba'), ('Maroko', 'Rabat'),
            ('Polska', 'Poznań'), ('Polska', 'Gdańska'), ('Polska', 'Wrocław'),
            ('Polska', 'Warszawa'), ('Polska', 'Kraków'), ('Polska', 'Katowice')]


def __get_test_players_positions():
    return [PlayerPositionChoice.GOALKEEPER_1, PlayerPositionChoice.CENTRAL_DEFENDER_4,
            PlayerPositionChoice.CENTRAL_DEFENDER_5, PlayerPositionChoice.SIDE_DEFENDER_3,
            PlayerPositionChoice.SIDE_DEFENDER_2, PlayerPositionChoice.DEFENSIVE_HELP_6,
            PlayerPositionChoice.SIDE_HELP_7, PlayerPositionChoice.SIDE_HELP_11,
            PlayerPositionChoice.ATTACKER_9, PlayerPositionChoice.MIDDLE_HELP_8,
            PlayerPositionChoice.MIDDLE_HELP_10]


def __get_test_players_statuses():
    return [PlayerStatusChoice.OBSERVATION, PlayerStatusChoice.INAPPROPRIATE, PlayerStatusChoice.TEST]


def __get_test_players_dominant_legs():
    return [PlayerDominantLegChoice.LEFT, PlayerDominantLegChoice.RIGHT, PlayerDominantLegChoice.NONE]


def __get_random_from_list(elements):
    return elements[randint(0, len(elements) - 1)]


def create_test_players():
    leagues = create_test_leagues()
    teams = create_test_teams()
    names = __get_test_players_names()
    surnames = __get_test_players_surnames()
    countries_with_cities = __get_test_players_countries_with_cities()
    positions = __get_test_players_positions()
    statuses = __get_test_players_statuses()
    dominant_legs = __get_test_players_dominant_legs()

    for i in range(100):
        league = __get_random_from_list(leagues)
        team = __get_random_from_list(teams)
        name = __get_random_from_list(names)
        surname = __get_random_from_list(surnames)
        country_with_city = __get_random_from_list(countries_with_cities)
        position = __get_random_from_list(positions)
        status = __get_random_from_list(statuses)
        dominant_leg = __get_random_from_list(dominant_legs)
        birth_date = date(randint(1990, 2010), randint(1, 12), randint(1, 28))

        Player.objects.get_or_create(name=name, surname=surname, position=position,
                                     birth_date=birth_date, country=country_with_city[0],
                                     city=country_with_city[1], dominant_leg=dominant_leg,
                                     is_active=True, team=team, league=league, status=status)
