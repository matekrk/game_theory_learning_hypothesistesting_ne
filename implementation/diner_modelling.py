from numpy import full
import pygambit as pg

n = 5 # n the number of players
a = 10 # Let a represent the joy of eating the expensive meal,
b = 6 # b the joy of eating the cheap meal,
k = 7 # k is the cost of the expensive meal,
l = 2 # l the cost of the cheap meal,

assert k-l > a-b

g = pg.Game.new_table([n,n])
g.title = "A simple Unscrupulous diner's dilemma example"

g.players[0].label = "Alice"
g.players[1].label = "Bob"
g.players[2].label = "Caley"
g.players[3].label = "David"
g.players[4].label = "Ester"
#TODO: For more players

for i in range(n):
    g.players[i].strategies[0].label = "Cooperate" # Cheap
    g.players[i].strategies[1].label = "Defect" # Expensive

strategies_list = []
for i in range(n):
    strategies_list.append(g.players[i].strategies)

game = pg.new_table(strategies_list)

menu = dict()
menu[0] = 6 #b
menu[1] = 10 #a

pleasure = dict()
pleasure[0] = 2 #l
pleasure[1] = 7 #k


#TODO: For more players better
for i_a in range(2):
    for i_b in range(2):
        for i_c in range(2):
            for i_d in range(2):
                full_other_cost = 1/n * (menu[i_a] + menu[i_b] + menu[i_c] + menu[i_d])
                for i_e in range(2):
                    g[i_a, i_b, i_c, i_d, i_e][4] = pleasure[i_e] - full_other_cost - (1/n) * menu[i_e]

for i_e in range(2):
    for i_a in range(2):
        for i_b in range(2):
            for i_c in range(2):
                full_other_cost = 1/n * (menu[i_e] + menu[i_a] + menu[i_b] + menu[i_c])
                for i_d in range(2):
                    g[i_a, i_b, i_c, i_d, i_e][3] = pleasure[i_d] - full_other_cost - (1/n) * menu[i_d]

for i_d in range(2):
    for i_e in range(2):
        for i_a in range(2):
            for i_b in range(2):
                full_other_cost = 1/n * (menu[i_d] + menu[i_e] + menu[i_a] + menu[i_b])
                for i_c in range(2):
                    g[i_a, i_b, i_c, i_d, i_e][2] = pleasure[i_c] - full_other_cost - (1/n) * menu[i_c]

for i_c in range(2):
    for i_d in range(2):
        for i_e in range(2):
            for i_a in range(2):
                full_other_cost = 1/n * (menu[i_c] + menu[i_d] + menu[i_e] + menu[i_a])
                for i_b in range(2):
                    g[i_a, i_b, i_c, i_d, i_e][1] = pleasure[i_b] - full_other_cost - (1/n) * menu[i_b]

for i_b in range(2):
    for i_c in range(2):
        for i_d in range(2):
            for i_e in range(2):
                full_other_cost = 1/n * (menu[i_b] + menu[i_c] + menu[i_d] + menu[i_e])
                for i_a in range(2):
                   g[i_a, i_b, i_c, i_d, i_e][0] = pleasure[i_a] - full_other_cost - (1/n) * menu[i_a]

"""
Consider an arbitrary set of strategies by a player's opponent. 
Let the total cost of the other players' meals be x. 
The cost of ordering the cheap meal is 1/n * x + 1/n * l
and the cost of ordering the expensive meal is 1/n * x + 1/n * k. 
So the utilities for each meal are a - 1/n*x - 1/n*k for the expensive meal 
and b - 1/n*x - 1/n*l for the cheaper meal. 
By assumption, the utility of ordering the expensive meal is higher. 
Remember that the choice of opponents' strategies was arbitrary and that the situation is symmetric. 
This proves that the expensive meal is strictly dominant and thus the unique Nash equilibrium.

If all the individuals had ordered the cheap meal, the utility of every player would have been b-l (>a-k)
"""

list(g.contingencies)
for profile in g.contingencies:
    print(profile, g[profile][0], g[profile][1], g[profile][2], g[profile][3], g[profile][4])

p = g.mixed_strategy_profile()
print(list(p))

#p = g.mixed_behavior_profile()
#p[g.players[0]]
#p[g.players[0].infosets[0]]
#p[g.players[0].infosets[0].actions[0]]


solver = pg.nash.ExternalEnumMixedSolver()
res = solver.solve(g)
print(res)
#pg.nash.lcp_solve(g, use_strategic=True, rational=True)

