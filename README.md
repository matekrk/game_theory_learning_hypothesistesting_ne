# game_theory_learning_hypothesistesting_ne
##  Game Theory IASD 2022 FosterYoung Learning Hypothesis Testing NE

### Plan for presentation:

+ introduce to framework - game theory and setup: non-collaborative, repeated games eps-best replies + (1-eps) of time eps-eq.
+ question posed: are there learning strategies that come close to equilibrium play of repeated game? important but challenging problem, because social systems are self-referential: the act of learning changes the thing to be learned.
+ Feedback loop: While holding a hypothesis, the hypothesis tester is forced to take actions that his opponent can observe. If the hypothesis tester is rational, these actions must bear a particular relationship to the hypothesis. This means that the opponents can make inferences about the tester’s current hypothesis, and hence his future actions, which may cause them to alter their future actions, thus perhaps invalidating the tester’s hypothesis.
    + “grain of reflection”: if player i intends to use a strategy, then she should not rule out the possibility that player j will adopt a best reply to her strategy. In other words, the support of a player’s beliefs should include all best replies to the player’s own strategy
+ present previous Foster&Young results about the problem of reaching equils of some games.
    + no difficulty in constructing dynamic algorithms that converge to NE of the stage game. given eps, simply search the space of mixed strategies until one finds eps-equilibrium of the stage game, then eps/2 etc. -> inf. Not solution! not decentralized learning processes (requires coordinated search), payoffs common knowledge (not robust), ignores desire of players to maximize their playoff as learning process.
    + pre: assumptions (not many (not strong!) here: 2 properties of testers, continuity w.r.t utility, similar amount of data, memory-based models)
    + fictitious play (special classes: zero-sum, dominance, potential games)
    + bayesian rational players can learn to play Nash when distri of payoff-types is common knowledge
    + an alternative approach to learning called prospecting in which players are rational and good predictors, but beliefs have a small random component.
+ hypothesis testing. 4 steps. type I - hypothesis sufficiently close to the truth -> rejecting close to 0. type II - hypothesis far from truth, test should reject with probability close to 1.
+ memory (for hypothesis), strategies no memory, bounded rationality, approximation
+ how to select new hypothesis? flexible+conservative
+ inference given model how to respond
+ vocabulary
+ theorem: dividing into subproblems as in report
+ proofs [until here it was only intuition!] only sketch of proofs (or the idea used there since the skeleton is in the previous point)
+ beliefs: naive no allowance for the possibility of change when rejecting a test. but because of cpnservativity - hypothesis testing strategies are eps-best reply to their belief
+ as in SA change of params over time (convergence in probability)
+ summarization -> what we proven!

Somehow this may be useful: http://www.cs.uu.nl/docs/vakken/maa/2010-11/slides/student/MAA_slides_HypothesisTesting_Rob.pdf