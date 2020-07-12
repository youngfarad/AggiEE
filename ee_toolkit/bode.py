from scipy import signal as sci
import matplotlib.pyplot as plt

class Bode(object):
	def __init__(self, t_func):
		sys = sci.TransferFunction(t_func["num"],t_func["denom"])
		self.signal = sci.bode(sys)
		
	def plot(self):
		w = self.signal[0]
		mag = self.signal[1]
		phase = self.signal[2]
		plt.figure()
		plt.semilogx(w, mag)    # Bode magnitude plot
		plt.figure()
		plt.semilogx(w, phase)  # Bode phase plot
		plt.show()

b = Bode({"num": [1], "denom" : [1,1]})
b.plot()