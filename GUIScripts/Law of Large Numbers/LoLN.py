# Import Packages
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
import mplcyberpunk


options = ["Law of Large Numbers"]
choice = st.sidebar.selectbox("Select", options)

# -- LAW OF LARGE NUMBERS --
if choice == 'Law of Large Numbers':


	st.title('Law of Large Numbers')

	st.write('\n')

	st.write('Law of Large Numbers states that if we take enough number of samples from a population, the mean of the sample distribution is close to the Population Mean')
	st.write("In other words, if we take a Large number of sampels from a population and take their means, the distribution of their means will be normally distributed with center at the Popultion Mean. Let's understand this with an example:")
	st.write("\n")
	st.write("First, Enter random numerical data")


	try:
		raw_data = st.text_input('Enter the Data', value = 0)
		raw_data = raw_data.strip()
		data = raw_data.replace(" , ", " ").replace(", ", " ").replace(" ,", " ").replace(" ", ',').split(',')
		x = [float(i) for i in data]

		popmean = np.mean(x)
		if popmean:
			st.write("\n")
			st.write("\n")
			st.write("Now, enter the number of Samples you want to take (for example: 100, 200 etc.)")

			try:
				# number of samples
				Expr = st.text_input('Enter Number of Samples', value = 0, key = 'expr1')
				Expr = int(Expr)

				samp_Mean = np.zeros(Expr)

				for i in range(Expr):
				  sample = np.random.choice(x, size = 15, replace = True)
				  samp_Mean[i] = np.mean(sample)

				plot = st.checkbox("Show Plot", key = 'plot_small') 

				st.write("\n")
				st.write("\n")

				if plot:
					plt.style.use("cyberpunk")

					fig, ax = plt.subplots()
					sns.distplot(samp_Mean, bins = 20)
					ax.plot([popmean, popmean], [0, 2])
					plt.xlim((np.mean(samp_Mean)-2.0, (np.mean(samp_Mean)+2.0)))
					plt.ylim([0, popmean/2])
					st.pyplot(fig)

				st.write('\n')
				st.write('\n')
				st.write('Now try giving a larger number of samples (For example: 100000, 200000)')

				# number of sampels -- 2
				try:
					Expr2 = st.text_input('Enter Number of Samples', value = 0, key = 'expr2')
					Expr2 = int(Expr2)
					
					samp_Mean = np.zeros(Expr2)

					for i in range(Expr2):
					  sample = np.random.choice(x, size = 15, replace = True)
					  samp_Mean[i] = np.mean(sample)

					plot = st.checkbox("Show Plot", key = 'plot_large') 

					st.write("\n")

					if plot:
						plt.style.use("cyberpunk")

						fig, ax = plt.subplots()
						sns.distplot(samp_Mean, bins = 20)
						ax.plot([popmean, popmean], [0, 2])
						plt.xlim((np.mean(samp_Mean)-2.0, (np.mean(samp_Mean)+2.0)))
						st.pyplot(fig)

						st.write("\n")	
						st.write('\n')
						st.write('When we took a lesser number of samples, the Distirbution was less normal, but when we took a large number of samples, it produces a Normal Distribution close to the Population.')
						st.write("In a Normal Distrbution, the mean is at the center. Thus, if we able to produce a Normal Sample Distribution around the Population Mean, the Mean of the Distrtibution will be equal to Population Mean.")

				except:
					st.write('Enter Valid Number of Samples')

			except:
				st.write('Enter Valid Number of Samples')
	
	except:
		st.write('Enter Valid Numeric Data. (Use commas or spaces to differentiate between numerical data.')