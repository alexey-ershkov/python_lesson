from operator import itemgetter


def do_auction(recs):
    return sorted(recs, key=itemgetter('price'), reverse=True)
