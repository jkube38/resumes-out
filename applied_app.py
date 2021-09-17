'''The applied apps keep track of the companies and positions I've applied to
   for a quick search to make sure it was not already applied to'''

__author__ = "Jordan Kubista"

import sys
import argparse
from applied import applied_to


def search_submissions(company):
    applied = False

    for sub in applied_to:
        if sub[0] == company:
            print(f'You have applied at {company} for a {sub[1]} position!')
            if sub[2] is False:
                print(f'You have not heard anything from {company}')
            else:
                print(f'{company} has sent you a rejection letter!')
            applied = True

    if applied is False:
        print(f'{company} is not in your list of resume submissions!')


def total_submissions(applied_list):
    total_resumes = len(applied_list)
    print(f'You have submitted {total_resumes} resumes!')


def create_parser():
    parser = argparse.ArgumentParser(description='''Search company and positions
        and positions applied for''')
    parser.add_argument('-s', '--search', help='''Enter company name to search for
        resume submissions to avoid multiple resume submissions to the
        same company''')
    return parser


def main(args):
    '''Initiates the Resumes Out program'''
    parser = create_parser()
    ns = parser.parse_args(args)

    search = ns.search

    if not ns:
        parser.print_usage()
        print(ns)
        sys.exit(1)

    if len(args) == 0:
        total_submissions(applied_to)
    elif search:
        search_submissions(search)


if __name__ == '__main__':
    main(sys.argv[1:])
