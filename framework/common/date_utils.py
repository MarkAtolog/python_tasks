from calendar import Calendar
from datetime import date, datetime, timedelta


class DateUtils:
    @staticmethod
    def calculate_closest_date(target_date):
        target_month = target_date["Month"]
        target_day = target_date["Day"]
        deltas = {}
        for year in range(date.today().year - 2, date.today().year + 3):
            for possible_date in Calendar().itermonthdates(year, target_month):
                if possible_date.day == target_day and possible_date.month == target_month:
                    deltas[possible_date] = possible_date - date.today()
        closest_date = min(deltas, key=lambda x: abs(deltas[x]))
        return closest_date

    @staticmethod
    def date_to_string(date_to_convert, given_format):
        string = date_to_convert.strftime(given_format)
        return string

    @staticmethod
    def string_to_datetime(date_string, given_format):
        result_date = datetime.strptime(date_string, given_format)
        return result_date

    @staticmethod
    def get_delta(delta: dict):
        weeks = delta["weeks"]
        days = delta["days"]
        hours = delta["hours"]
        minutes = delta["minutes"]
        seconds = delta["seconds"]

        return timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
