# code inspired by https://gist.github.com/n0m4dz/ee41d4ca84e2630e70c6

from datetime import timedelta

DAY = {
    'singular': 'day',
    'plural1': 'days',
    'plural2': 'days'
}

MONTH = {
    'singular': 'month',
    'plural1': 'month',
    'plural2': 'month'
}

YEAR = {
    'singular': 'year',
    'plural1': 'years',
    'plural2': 'years'
}

HOUR = {
    'singular': 'hour',
    'plural1': 'hours',
    'plural2': 'hours'
}

MINUTE = {
    'singular': 'minute',
    'plural1': 'minutes',
    'plural2': 'minutes'
}

SECOND = {
    'singular': 'second',
    'plural1': 'seconds',
    'plural2': 'seconds'
}


def _pluralize(quantity, dictionary):

    remainder = quantity % 10

    if isinstance(dictionary, dict):
        if 1 < remainder < 5:
            return dictionary['plural1']
        elif quantity == 1:
            return dictionary['singular']
        else:
            return dictionary['plural2']
    else:
        raise TypeError('Nie podano słownika')


def localize(timespan):
    if isinstance(timespan, timedelta):
        days = int(timespan.days % 365) % 30
        months = int((timespan.days % 365) / 30)
        years = int(timespan.days / 365)
        hours = int(timespan.seconds / 3600)
        minutes = int(timespan.seconds / 60) % 60
        seconds = timespan.seconds % 60

        days_str = _pluralize(days, DAY)
        months_str = _pluralize(months, MONTH)
        years_str = _pluralize(years, YEAR)
        hours_str = _pluralize(hours, HOUR)
        minutes_str = _pluralize(minutes, MINUTE)
        seconds_str = _pluralize(seconds, SECOND)

        return_string = ""

        if years != 0:
            return_string += "{} {}".format(years, years_str)
        if months != 0:
            return_string += " {} {}".format(months, months_str)
        if days != 0:
            return_string += " {} {}".format(days, days_str)
        if hours != 0:
            return_string += " {} {}".format(hours, hours_str)
        if minutes != 0:
            return_string += " {} {}".format(minutes, minutes_str)
        if seconds != 0:
            return_string += " {} {}".format(seconds, seconds_str)

        return return_string
    else:
        raise TypeError('Incorrect input type')
