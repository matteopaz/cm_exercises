


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

initial_state = {"a": -0.45, "b": -0.05, "c": 0}
def da_dt(t, state):
    return state["a"] + 1

def db_dt(t, state):
    return state["b"] + state["a"]

def dc_dt(t, state):
    return 2 * state["b"] + 3 * t

derivatives = {"a": da_dt, "b": db_dt, "c": dc_dt}
estimator = EulerEstimator(derivatives)

initial_pt = (-0.4, initial_state)

step_size = 2
num_steps = 3

der = estimator.eval_derivative(initial_pt)
ests = estimator.estimate(initial_pt, step_size, num_steps)

print(der)
print(ests)