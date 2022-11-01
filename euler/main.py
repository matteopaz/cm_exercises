import matplotlib.pyplot as plt
class EulerEstimator:
    def __init__(self, derivatives):
        self.df = derivatives
    
    def __copy(self, state):
        new_state = {}
        for x in state:
            new_state[x] = state[x]
        return new_state
    
    def eval_derivative(self, pt):
        d = {}
        t = pt[0]
        state = pt[1]
        for x in state:
            d[x] = self.df[x](t, state)
        return d

    def estimate(self, initial_pt, step_size, num_steps):
        t = initial_pt[0]
        state = self.__copy(initial_pt[1])
        history = []
        for i in range(num_steps):
            history.append([t, self.__copy(state)])
            d = self.eval_derivative((t, state))
            for x in state:
                state[x] += step_size * d[x]
            t += step_size
        return history

# initial_state = {"S": 1000, "I": 1, "R": 0}

# def dS_dt(t, state):
#     return state["S"] * -0.01 * state["I"] * 0.03

# def dI_dt(t, state):
#     return  -dS_dt(t, state) - dR_dt(t, state)

# def dR_dt(t, state):
#     return 0.02*state["I"]

# derivatives = {"S": dS_dt, "I": dI_dt, "R": dR_dt}
# estimator = EulerEstimator(derivatives)

# initial_pt = (0, initial_state)

# step_size = 0.1
# num_steps = 1000

# der = estimator.eval_derivative(initial_pt)
# ests = estimator.estimate(initial_pt, step_size, num_steps)

# print(der)
# # print(ests)


# def plot(ests):
#     t = []
#     S = []
#     I = []
#     R = []
#     for est in ests:
#         t.append(est[0])
#         S.append(est[1]["S"])
#         I.append(est[1]["I"])
#         R.append(est[1]["R"])

#     # color theme blue, red, green
#     plt.plot(t, S, label="S", color="#1f77b4")
#     plt.plot(t, I, label="I", color="#ff7f0e")
#     plt.plot(t, R, label="R", color="#2ca02c")
#     plt.legend()
#     plt.show()

# plot(ests)