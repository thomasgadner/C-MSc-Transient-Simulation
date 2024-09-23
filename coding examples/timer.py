import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def ramp(t): return t % 1

def sawtooth(t,freq):
    return  signal.sawtooth(2 * np.pi * freq * t, 0.5)/2 + 0.5

def carrier(t,freq,centeraligned=False):
   return sawtooth(t,freq) if centeraligned else ramp(t)

def pwm(t,vek,D,):
  '''generate PWM signals with duty cycle D'''
  return ( vek[t] <= D ) * 1.0

def plot_pwm(t,vek,pwm_sig):
    plt.figure(figsize=(8, 4))
    plt.plot(t, vek, t, pwm_sig)
    plt.title("Sawtooth Waveform")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()



if __name__=="__main__":
    t = np.arange(0,10,0.000005)  # time vector
    vek = carrier(t,100,centeraligned=True) # carrier signal
    pwm_sig = np.zeros(len(t)) # pwm signal

    for i in range(0, len(t)):  # pwm signal
        pwm_sig[i] = (pwm(i,vek,0.1))   # duty cycle 0.1    

    plt.figure(figsize=(8, 4))
    plt.plot(t, vek, t, pwm_sig)
    plt.title("Sawtooth Waveform")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()


