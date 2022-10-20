def filter_by_geo_and_gender(recs, gender, geo):
    filtered_recs = []
    for rec in recs:
        if rec['geo'] == geo and rec['gender'] == gender:
            filtered_recs.append(rec)

    return filtered_recs
