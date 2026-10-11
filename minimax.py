class HalvingGame():
    def __init__(self, N):
        self.N = N

    def startState(self):
        return (+1, self.N)
    
    def isEnd(self, state):
        player, number = state
        return number == 0

    def utility(self, state):
        player, number = state
        assert number == 0
        return number * float("inf")

    def actions(self, state):
        return ['/', '-']

    def player(self, state):
        player, number = state
        return player

    def succ(self, state, action):
        player, number = state
        if action == '-':
            return (-player, number - 1)
        elif action == '/':
            return (-player, number // 2)

def humanPolicy(game, state):
    while True:
        action = input('Input action: ')
        if action in game.actions(state):
            return action

def minimaxPolicy(game, state):
    def recurse(state):
        if game.isEnd(state):
            return (game.utility(state), 'state')
        choices = [(recurse(game.succ(state, action)), action) for action in game.actions(state)]
        if game.player == +1:
            return max(choices)
        if game.player == -1:
            return min(choices)
        