vote_list = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice']

vote_dict = {
    'Alice': 3,
    'Bob': 2,
    'Charlie': 1
}

vote_list_dict =[
    {
        'candidate_id': 'Alice',
        'votes': 65,
        'priority_iflost': 'Jessica',
        'priority_ifwon': 'Jessica'
    },
    {
        'candidate_id': 'Jessica',
        'votes': 1,
        'priority_iflost': 'Alice',
        'priority_ifwon': 'Alice'
    },
    {
        'candidate_id': 'Bob',
        'votes': 16,
        'priority_iflost': 'Charlie',
        'priority_ifwon': 'Charlie'
    },
    {
        'candidate_id': 'Charlie',
        'votes': 18,
        'priority_iflost': 'Bob',
        'priority_ifwon': 'Bob'
    }
]


def find_winner(votes):
    if not votes:
        return None
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
    winner = max(vote_counts, key=vote_counts.get)
    return winner

def find_winner_dict(votes):
    if not votes:
        return None
    winner = max(votes, key=votes.get)
    return winner

def find_winner_list_dict(votes):
    
    votes = sorted(votes, key=lambda x: x['votes'], reverse=True)
    if not votes:
        return None
    num_of_winners = 3
    min_winner_score = 100 // num_of_winners #33
    potential_winners = []
    
    for candidate in votes:
        if candidate['votes'] > min_winner_score:
            potential_winners.append(candidate['candidate_id'])
            for vote in votes:
                if vote['candidate_id'] == candidate['priority_ifwon']:
                    vote['votes'] += candidate['votes'] - min_winner_score
                    break
        elif candidate['votes'] == min_winner_score:
            potential_winners.append(candidate['candidate_id'])
        else:
            for vote in votes:
                if vote['candidate_id'] == candidate['priority_iflost']:
                    vote['votes'] += candidate['votes']
                    break
        continue
            
    return potential_winners


print(find_winner_list_dict(vote_list_dict))