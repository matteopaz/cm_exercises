from main import *
import math
import matplotlib.pyplot as plt

###############################
### constants


C = 1.0
V_Na = 115
V_K = -12
V_L = 10.6

G_NA = 120
G_K = 36
G_L = 0.3


###############################
### main variables: V, n, m, h

def dV_dt(t,x):
	return (1 / C) * (s(t,x) - I_Na(t,x) - I_K(t,x) - I_L(t,x))

def dn_dt(t,x):
	n = x['n']
	return alpha_n(t,x) * (1 - n) - beta_n(t,x) * n

def dm_dt(t,x):
	m = x['m']
	return alpha_m(t,x) * (1 - m) - beta_m(t,x) * m

def dh_dt(t,x):
	h = x['h']
	return alpha_h(t,x) * (1 - h) - beta_h(t,x) * h

###############################
### intermediate variables: alphas, betas, stimulus (s), currents (I's), ...

def alpha_n(t,x):
	v = x['V']
	return 0.01*(10 - v)/(math.exp(0.1*(10-v)) - 1)

def beta_n(t,x):
	v = x['V']
	return 0.125 * math.exp(-v/80)

def alpha_m(t,x):
	v = x['V']
	return 0.1*(25 - v)/(math.exp(0.1*(25 - v)) - 1)

def beta_m(t,x):
	v = x['V']
	return 4 * math.exp(-v/18)

def alpha_h(t,x):
	v = x['V']
	return 0.07 * math.exp(-v/20)

def beta_h(t,x):
	v = x['V']
	return 1/(math.exp(0.1*(30 - v)) + 1)

def s(t, x):

	intervals = [
		(10, 11, 150),
		(20, 21, 150),
		(30, 40, 150),
		(50, 51, 150),
		(53, 54, 150),
		(56, 57, 150),
		(59, 60, 150),
		(62, 63, 150),
		(65, 66, 150),
	]
	for interval in intervals:
		if interval[0] <= t <= interval[1]:
			return interval[2]
	return 0

def I_Na(t,x):
	return g_Na(t,x) * (x['V'] - V_Na)
def I_K(t,x):
	return g_K(t,x) * (x['V'] - V_K)
def I_L(t,x):
	return g_L(t,x) * (x['V'] - V_L)

def g_Na(t,x):
	return G_NA * x['m']**3 * x['h']
def g_K(t,x):
	return G_K * x['n']**4
def g_L(t,x):
	return G_L

################################
### input into EulerEstimator
V_0 = 0
n_0 = alpha_n(0,{'V':V_0})/(alpha_n(0,{'V':V_0}) + beta_n(0,{'V':V_0}))
m_0 = alpha_m(0,{'V':V_0})/(alpha_m(0,{'V':V_0}) + beta_m(0,{'V':V_0}))
h_0 = alpha_h(0,{'V':V_0})/(alpha_h(0,{'V':V_0}) + beta_h(0,{'V':V_0}))

initial_state = {"V": V_0, "n": n_0, "m": m_0, "h": h_0}

derivatives = {
	'V': dV_dt,
	'n': dn_dt,
	'm': dm_dt,
	'h': dh_dt
}

initial_point = (0, initial_state)

estimator = EulerEstimator(derivatives)
ests = estimator.estimate(initial_point, 0.01, 8000)

def plot(ests):
	t = []
	V = []
	n = []
	m = []
	h = []
	stimuli = []
	for est in ests:
		t.append(est[0])
		stimuli.append(s(est[0], est[1]))
		V.append(est[1]['V'])
		n.append(est[1]['n'])
		m.append(est[1]['m'])
		h.append(est[1]['h'])
	
	plt.plot(t, V, label='V')
	plt.plot(t, n, label='n')
	plt.plot(t, m, label='m')
	plt.plot(t, h, label='h')
	plt.plot(t, stimuli, label='s')

	plt.legend()
	plt.show()

plot(ests)
