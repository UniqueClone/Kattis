tests = int(input())

for i in range(tests):
    noOfCandidates = int(input())
    candidates=[]
    totalVotes=0

    for n in range(noOfCandidates):
        candidates.append(int(input()))
        totalVotes += candidates[-1]

    winner = candidates.index(max(candidates))+1
    candidates.sort()

    if(candidates[-1] == candidates[-2]):
        print("no winner")
    elif(max(candidates) > (totalVotes / 2)):
        print("majority winner " + str(winner))
    else:
        print("minority winner " + str(winner))
