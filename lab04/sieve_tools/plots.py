import numpy as np 
import matplotlib.pyplot as plt
from sieve_tools import sieve

def proportion_plot(nmax):
    all_nmax=np.arange(100,nmax,100)
    all_proportions=sieve.proportion_primes(nmax)
    plt.plot(all_nmax, all_proportions)
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")
    plt.plot(all_nmax, all_proportions)
    plt.xscale("log")
    plt.yscale("log")