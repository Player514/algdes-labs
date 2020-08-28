import sys
import re

def parse_stdin():
    finding_candidates = True
    count = 0
    reachers = {}           # Pursuers attempting to match with their preferences
    settlers = {}           # Pursued settling for an approaching candidate
    preferences = {}        # The preferences for all candidates
    candidate_count = 0
    ranking = {}            # A rank[settler][reacher] instant lookup for settlers' preference

    for line in sys.stdin:
        line = line.strip()
        
        if (line.startswith('#')):
            continue

        if '=' in line:
            count = int(line[-1])
            continue

        if (line == ''): 
            finding_candidates = False

        candidate_match = re.findall('(\d+) (.*)', line)
        if candidate_match and finding_candidates:
            index = candidate_match[0][0]
            name = candidate_match[0][1]
            if candidate_count % 2 == 0: 
                reachers[index] = name
            else:
                settlers[index] = name
            candidate_count += 1

        preference_match = re.findall('(\d+): (.*)', line)
        if preference_match: 
            prefs = preference_match[0][1].split(' ')
            preferences[preference_match[0][0]] = prefs
            if preference_match[0][0] in settlers:
                ranking[preference_match[0][0]] = {}
                for index, preference in enumerate(prefs):
                    ranking[preference_match[0][0]][preference] = index

    return reachers, settlers, preferences, ranking


def stable_match(reachers, settlers, preferences, ranking):
    matched_reachers = {}
    matched_settlers = {}
    not_matched = set(reachers.keys())

    while not_matched:
        reacher = not_matched.pop()
        if preferences[reacher]:
            # Use preference stack for getting reacher preferences in order (constant time)
            preference = preferences[reacher].pop(0) 

            if preference not in matched_settlers: 
                matched_reachers[reacher] = preference
                matched_settlers[preference] = reacher
            else: 
                settled_with = matched_settlers[preference]
                # Use preference lookup table for getting settler preferences (constant time)
                likes_current_more = ranking[preference][settled_with] < ranking[preference][reacher]
                if (likes_current_more):
                    not_matched.add(reacher)
                else: 
                    matched_reachers[reacher] = preference
                    matched_settlers[preference] = reacher
                    not_matched.add(settled_with)
    
    result = list(matched_reachers.items())
    return result


def print_result(results, reachers, settlers):
    for result in results: 
        to_print = f"{reachers[result[0]]} -- {settlers[result[1]]}"
        print(to_print)

reachers, settlers, preferences, ranking = parse_stdin()
result = stable_match(reachers, settlers, preferences, ranking)
print_result(result, reachers, settlers)