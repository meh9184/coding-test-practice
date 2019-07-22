def solution(participant, completion):

    if len(participant) == len(set(participant)):
        return (set(participant) - set(completion)).pop()

    else:
        participant.sort()
        completion.sort()

        for i, j in zip(participant, completion):
            if i != j:
                return i

        return participant[-1]


# participant = ['mislav', 'stanko', 'mislav', 'ana']
# completion = ['stanko', 'mislav', 'ana']

participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']



print(solution(participant, completion))
