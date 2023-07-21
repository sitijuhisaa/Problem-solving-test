def dense_ranking(scores, gits_scores):
    unique_scores = sorted(set(scores), reverse=True)
    ranking = {}

    for i, score in enumerate(unique_scores, start=1):
        ranking[score] = i

    gits_ranks = [ranking.get(score, i + 1) for i, score in enumerate(gits_scores)]
    return gits_ranks

# Contoh penggunaan fungsi
total_players = 7
all_scores = [100, 100, 50, 40, 40, 20, 10]
gits_games = 4
gits_scores = [5, 25, 50, 120]

result = dense_ranking(all_scores, gits_scores)
print(result)

