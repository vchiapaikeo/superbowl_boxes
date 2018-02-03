import argparse
import logging
import numpy as np
import sys

from random import randint, shuffle
from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def parse_args():
    parser = argparse.ArgumentParser(
        prog=__name__,
        description='Randomly generates superbowl boxes for '
            'you and your friends.')

    parser.add_argument(
        '--friends',
        type=str,
	required=True,
        help='Comma separated list of friend names.')

    parser.add_argument(
        '--num-boxes',
        type=int,
	default=100,
        help='Comma separated list of friend names.')

    return parser.parse_args()


def format_results(results: List[str]) -> str:
    formatted = ''
    for i, name in enumerate(results):
	# Newline every 10 names
        num = i + 1
        formatted += '{num}: {name} '.format(**locals())
        if num % 10 == 0:
            formatted += '\n'
    return formatted


def get_random_names(friends: List[str], num_boxes: int) -> List[str]:
    # Did this earlier but that is wrong
    # results = np.random.choice(
    #     friends,
    #     num_boxes,
    #     p=([1 / num_friends] * num_friends))

    shuffle(friends)
    num_friends = len(friends)
    names_to_randomize = []
    for i in range(0, num_boxes):
        idx = i % num_friends
        names_to_randomize.append(friends[idx])

    random_names = []
    for i in range(0, num_boxes):
        random_idx = randint(0, num_boxes - i)
        assignment = names_to_randomize.pop(random_idx - 1)
        random_names.append(assignment)

    return random_names


def gen_results(friends: List[str], num_boxes: int) -> List[List[int]]:
    results = get_random_names(friends, num_boxes)
    formatted = format_results(results)
    reshaped_results = np.reshape(results, (-1, 10))

    logger.info(
	'Final Results: \n'
	'{}'.format(formatted))
    return reshaped_results


if __name__ == "__main__":
    options = parse_args()
    friends = [name.strip() for name in options.friends.split(',')]
    logger.info('List of friends passed: {}'.format(friends))
    gen_results(friends, options.num_boxes)

