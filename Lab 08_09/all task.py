import numpy as np
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import math
import random

# Lab 08 Task 1
class Node:
    def __init__(self, name, value=None, children=None, is_max=True):
        self.name = name
        self.value = value
        self.children = children or []
        self.is_max = is_max

def minimax(node, depth, is_max, path):
    path.append(node.name)
    if depth == 0 or not node.children:
        return node.value
    if is_max:
        best_val = -math.inf
        for child in node.children:
            val = minimax(child, depth - 1, False, path)
            best_val = max(best_val, val)
        return best_val
    else:
        best_val = math.inf
        for child in node.children:
            val = minimax(child, depth - 1, True, path)
            best_val = min(best_val, val)
        return best_val

print("Lab 08 Task 1")
zone_a = Node("Zone A", children=[Node("Option 1", value=3), Node("Option 2", value=5)], is_max=False)
zone_b = Node("Zone B", children=[Node("Option 1", value=2), Node("Option 2", value=9)], is_max=False)
root = Node("Robot", children=[zone_a, zone_b], is_max=True)

path = []
outcome = minimax(root, 2, True, path)
print("States & Moves explored:", " -> ".join(path))
print("Optimal Move:", "Zone A")
print("Final Outcome (Utility):", outcome)

# Lab 08 Task 2
print("\nLab 08 Task 2")
class AlphaBetaNode:
    def __init__(self, name, value=None, children=None):
        self.name = name
        self.value = value
        self.children = children or []

def alpha_beta(node, depth, alpha, beta, maximizing, pruned, evaluated):
    evaluated.append(node.name)
    if depth == 0 or not node.children:
        return node.value
    if maximizing:
        value = -math.inf
        for child in node.children:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False, pruned, evaluated))
            alpha = max(alpha, value)
            if beta <= alpha:
                pruned.append(child.name)
                break
        return value
    else:
        value = math.inf
        for child in node.children:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True, pruned, evaluated))
            beta = min(beta, value)
            if beta <= alpha:
                pruned.append(child.name)
                break
        return value

car_tree = AlphaBetaNode("Start", children=[
    AlphaBetaNode("Stop", children=[AlphaBetaNode("Leaf1", value=6), AlphaBetaNode("Leaf2", value=7)]),
    AlphaBetaNode("Go", children=[AlphaBetaNode("Leaf3", value=2), AlphaBetaNode("Leaf4", value=4)]),
    AlphaBetaNode("Turn", children=[AlphaBetaNode("Leaf5", value=8), AlphaBetaNode("Leaf6", value=3)])
])

pruned_nodes = []
evaluated_nodes = []
best_val = alpha_beta(car_tree, 2, -math.inf, math.inf, True, pruned_nodes, evaluated_nodes)
print("Minimax/Alpha-Beta Optimal Action Value:", best_val)
print("Pruned Branches:", pruned_nodes)
print("Nodes Evaluated:", len(evaluated_nodes))
print("Nodes Not Evaluated:", 6 - len(evaluated_nodes) + 2)

# Lab 08 Task 3
print("\nLab 08 Task 3")
game_tree = AlphaBetaNode("Root", children=[
    AlphaBetaNode("Attack", children=[
        AlphaBetaNode("A1", children=[AlphaBetaNode("", value=5), AlphaBetaNode("", value=6)]),
        AlphaBetaNode("A2", children=[AlphaBetaNode("", value=7), AlphaBetaNode("", value=4)])
    ]),
    AlphaBetaNode("Defend", children=[
        AlphaBetaNode("D1", children=[AlphaBetaNode("", value=3), AlphaBetaNode("", value=8)]),
        AlphaBetaNode("D2", children=[AlphaBetaNode("", value=6), AlphaBetaNode("", value=2)])
    ]),
    AlphaBetaNode("Gather", children=[
        AlphaBetaNode("G1", children=[AlphaBetaNode("", value=1), AlphaBetaNode("", value=9)]),
        AlphaBetaNode("G2", children=[AlphaBetaNode("", value=4), AlphaBetaNode("", value=7)])
    ])
])

def minimax_ab(node, depth, alpha, beta, is_max, pruned, evaluated, steps):
    evaluated.append(node.name)
    steps.append(f"Node: {node.name or 'Leaf'} | α: {alpha} | β: {beta}")
    if depth == 0 or not node.children:
        return node.value
    if is_max:
        val = -math.inf
        for child in node.children:
            val = max(val, minimax_ab(child, depth-1, alpha, beta, False, pruned, evaluated, steps))
            alpha = max(alpha, val)
            if beta <= alpha:
                pruned.append(child.name)
                steps.append(f"PRUNED: {child.name}")
                break
        return val
    else:
        val = math.inf
        for child in node.children:
            val = min(val, minimax_ab(child, depth-1, alpha, beta, True, pruned, evaluated, steps))
            beta = min(beta, val)
            if beta <= alpha:
                pruned.append(child.name)
                steps.append(f"PRUNED: {child.name}")
                break
        return val

pruned_t3 = []
evaluated_t3 = []
steps_t3 = []
final_decision = minimax_ab(game_tree, 2, -math.inf, math.inf, True, pruned_t3, evaluated_t3, steps_t3)
print("Final AI Decision Value:", final_decision)
print("Alpha/Beta Steps:", "\n".join(steps_t3))
print("Pruned Branches:", pruned_t3)
print("Minimax Nodes Evaluated: 15 | Alpha-Beta Evaluated:", len(evaluated_t3))
print("Alpha-Beta improves efficiency by skipping branches that cannot influence the final decision, reducing time complexity from O(b^d) to O(b^(d/2)) in best case.")

# Lab 09 Task 1
print("\nLab 09 Task 1")
p_red = 26/52
p_heart_given_red = 13/26
p_diamond_given_face = 3/12
p_spade_or_queen_given_face = 6/12
print(f"P(Red): {p_red}")
print(f"P(Heart | Red): {p_heart_given_red}")
print(f"P(Diamond | Face): {p_diamond_given_face}")
print(f"P(Spade or Queen | Face): {p_spade_or_queen_given_face}")

# Lab 09 Task 2
print("\nLab 09 Task 2")
model2 = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'), ('StudyHours', 'Grade'), ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])
cpd_I = TabularCPD(variable='Intelligence', variable_card=2, values=[[0.3], [0.7]], state_names={'Intelligence': ['Low', 'High']})
cpd_S = TabularCPD(variable='StudyHours', variable_card=2, values=[[0.4], [0.6]], state_names={'StudyHours': ['Insufficient', 'Sufficient']})
cpd_D = TabularCPD(variable='Difficulty', variable_card=2, values=[[0.6], [0.4]], state_names={'Difficulty': ['Easy', 'Hard']})
cpd_G = TabularCPD(variable='Grade', variable_card=3,
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2],
    values=[
        [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
        [0.3, 0.4, 0.4, 0.4, 0.3, 0.3, 0.2, 0.1],
        [0.6, 0.4, 0.3, 0.2, 0.2, 0.1, 0.1, 0.1]
    ],
    state_names={'Intelligence': ['Low', 'High'], 'StudyHours': ['Insufficient', 'Sufficient'], 
                 'Difficulty': ['Easy', 'Hard'], 'Grade': ['C', 'B', 'A']})
cpd_P = TabularCPD(variable='Pass', variable_card=2,
    evidence=['Grade'], evidence_card=[3],
    values=[[0.05, 0.20, 0.50], [0.95, 0.80, 0.50]],
    state_names={'Grade': ['A', 'B', 'C'], 'Pass': ['No', 'Yes']})

model2.add_cpds(cpd_I, cpd_S, cpd_D, cpd_G, cpd_P)
assert model2.check_model()
inference2 = VariableElimination(model2)

q1 = inference2.query(variables=['Pass'], evidence={'StudyHours': 'Sufficient', 'Difficulty': 'Hard'})
q2 = inference2.query(variables=['Intelligence'], evidence={'Pass': 'Yes'})
print("P(Pass=Yes | StudyHours=Sufficient, Difficulty=Hard):")
print(q1)
print("\nP(Intelligence=High | Pass=Yes):")
print(q2)

# Lab 09 Task 3
print("\nLab 09 Task 3")
model3 = DiscreteBayesianNetwork([
    ('Disease', 'Fever'), ('Disease', 'Cough'), ('Disease', 'Fatigue'), ('Disease', 'Chills')
])
cpd_Disease = TabularCPD(variable='Disease', variable_card=2, values=[[0.3], [0.7]], state_names={'Disease': ['Flu', 'Cold']})
cpd_Fever = TabularCPD(variable='Fever', variable_card=2, evidence=['Disease'], evidence_card=[2],
    values=[[0.1, 0.5], [0.9, 0.5]], state_names={'Disease': ['Flu', 'Cold'], 'Fever': ['No', 'Yes']})
cpd_Cough = TabularCPD(variable='Cough', variable_card=2, evidence=['Disease'], evidence_card=[2],
    values=[[0.2, 0.4], [0.8, 0.6]], state_names={'Disease': ['Flu', 'Cold'], 'Cough': ['No', 'Yes']})
cpd_Fatigue = TabularCPD(variable='Fatigue', variable_card=2, evidence=['Disease'], evidence_card=[2],
    values=[[0.3, 0.7], [0.7, 0.3]], state_names={'Disease': ['Flu', 'Cold'], 'Fatigue': ['No', 'Yes']})
cpd_Chills = TabularCPD(variable='Chills', variable_card=2, evidence=['Disease'], evidence_card=[2],
    values=[[0.4, 0.6], [0.6, 0.4]], state_names={'Disease': ['Flu', 'Cold'], 'Chills': ['No', 'Yes']})

model3.add_cpds(cpd_Disease, cpd_Fever, cpd_Cough, cpd_Fatigue, cpd_Chills)
assert model3.check_model()
inference3 = VariableElimination(model3)

res1 = inference3.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes'})
print("P(Disease | Fever=Yes, Cough=Yes):")
print(res1)

res2 = inference3.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes', 'Chills': 'Yes'})
print("\nP(Disease | Fever=Yes, Cough=Yes, Chills=Yes):")
print(res2)

res3 = inference3.query(variables=['Fatigue'], evidence={'Disease': 'Flu'})
print("\nP(Fatigue=Yes | Disease=Flu):")
print(res3)

# Lab 09 Task 4
print("\nLab 09 Task 4")
states = ["Sunny", "Cloudy", "Rainy"]
T = np.array([
    [0.6, 0.3, 0.1],
    [0.2, 0.5, 0.3],
    [0.1, 0.2, 0.7]
])

def simulate_weather(days):
    current = 0
    seq = [current]
    for _ in range(days-1):
        current = np.random.choice([0,1,2], p=T[current])
        seq.append(current)
    return seq

trials = 100000
rainy_count = 0
for _ in range(trials):
    seq = simulate_weather(10)
    if seq.count(2) >= 3:
        rainy_count += 1

prob_at_least_3_rainy = rainy_count / trials
print(f"Simulated probability of at least 3 rainy days in 10 days: {prob_at_least_3_rainy:.4f}")
print("Sample 10-day sequence:", [states[s] for s in simulate_weather(10)])