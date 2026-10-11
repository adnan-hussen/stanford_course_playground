class TransportationMDP():
    def __init__(self, N):
        self.N = N
    def startState(self):
        return 1
    def isEnd(self, state):
        return state == self.N
    def actions(self, state):
        result = []
        if state+1 <= self.N:
            result.append('walk')
        if state*2 <= self.N:
            result.append('tram')
        return result
    def succProbReward(self, state, action):
        result = []

        if action == 'walk':
            result.append((state + 1, 1, -1))
        if action == 'tram':
            result.append((state * 2, 0.5, -2))
            result.append((state, 0.5, -2))
        return result
    def discount(self):
        return 1
    def states(self):
        return range(1, self.N + 1)

def valueIteration(mdp):
    V = {}

    for state in mdp.states:
        V[state] = 0

    def Q(A, S):
        return sum(prob * (reward + mdp.discount() * V[newState]) for newState, prob, reward in mdp.succProbReward(S, A))

    
