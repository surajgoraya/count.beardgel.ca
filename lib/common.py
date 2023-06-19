import yaml
import os
import logging
import humanize
import datetime as dt
def get_counts():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '/static/countdown.yaml')
    try:
        with open(filename, "r") as stream:
            try:
                safe_yaml = yaml.safe_load(stream)
                for countdown_item in safe_yaml['Countdowns']:
                    countdown_item['friendly_date'] = humanize.naturaldelta(dt.datetime.strptime(countdown_item['date'], "%m-%d-%Y") - dt.datetime.now(), months=False, minimum_unit='seconds')
                return safe_yaml
            except yaml.YAMLError as exc:
                logging.error("Something went wrong parsing yaml data, it may be malformed")
                return None
    except FileNotFoundError as fne:
        logging.error("Something went wrong with finding the countdown file.")
        return None
