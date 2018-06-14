#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 14:52:54 2018

@author: kecooper
"""

def sqrt(N, x_n=1):
	for n in range(100):
		x_n = 0.5*((x_n) + (N/(x_n)))
		round(x_n, 6)
	if x_n == N**0.5:
		print("Correct Value")
	return x_n