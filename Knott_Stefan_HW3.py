#Stefan Knott
#HW 3
#Using the maximum subarray problem, find the best buy/sell dates of stocks
#Here 3 digit numbers for dates correspond to MDD -- MonthDayDay

#Find the difference between each neighboring element in the array passed, and returns an array of these values
def find_diffs(A):
	B = []
	for x in range(1, len(A)):
		B.append(A[x] - A[x-1])	
	return B

#Find best buy/sell date for a stock based on opening prices and dates
def stock_function(openPrice, dates):
	openPrice.reverse() #This accounts for the reverse order of the stock prices due to copying in from Excel
	daily_diff = find_diffs(openPrice) #finds difference between each day 
	buyDate, sellDate, monies = max_subarray(daily_diff) #look for max subarray
	print " BuyDate: ",  dates[buyDate], "Sell Date: ", dates[sellDate], "Gain per Share: ", monies, "\n"

#Max subarray function, keeps track of both lower and upper index of the subarray.  Taken from stackOverflow and slightly modified
def max_subarray(A):
    sellDate = 0
    best = cur = 0
    curi = starti = besti = 0
    for ind, i, in enumerate(A):
	if cur+i > 0:
		cur += i
	else:
		cur , curi = 0, ind+1
	if cur > best:
		starti, besti, best = curi, ind+1, cur

    return starti, besti, best

if __name__ == "__main__":

	Conoco = [80.46,80.84,81,79.5,78.24,79.21,78.23,78.76,79.47,79.94,79.78,81.14,80.98,81.06,80.87,80.89,80.88,80.73,80.33,80.68,80.57,80.19,79.65,80.95,80.26,81.12,81.19,80.52,81.73,79.69,80.83,79.65,81.44,80.76,81.91,84.22,85.25,85.01,86,86.16,86.68,86.12,84.93,84.88,84.9,86.02,85.22,85.63,85.13,85.52,84.91,86.07,85.98,85.84,85.73,85.81,86.25,85.81,85.75,85.59,84.65,86.02,85.59,85.11,84.27]

	Apple = [102.29,101.93,101.27,99.8,102.81,101.21,100.41,98.01,99.08,99.3,98.8,98.85,103.1,103.06,102.86,101.59,101.02,101.42,101.79,100.29,100.57,100.44,99.41,98.49,97.9,97.33,96.15,96.04,95.27,94.26,94.93,94.75,95.36,96.37,94.9,97.16,98.44,99.33,97.82,96.85,97.035,95.42,94.68,94.99,93.62,95.03,96.97,96.8,95.86,95.36,93.76,95.44,96.27,94.14,93.67,93.865,93.52,92.1,90.82,90.37,90.21,90.75,91.32,91.85,92.29]

	Copw = [0.0032,0.0053,0.0024,0.0039,0.0049,0.0038,0.0038,0.0032,0.0032,0.0031,0.004,0.0038,0.0038,0.0037,0.0031,0.0025,0.0036,0.002,0.0036,0.0036,0.0036,0.0035,0.0029,0.0042,0.0041,0.0041,0.0041,0.0035,0.0045,0.0042,0.0045,0.004,0.0055,0.0056,0.0082,0.0088,0.0071,0.0078,0.0058,0.0058,0.006,0.01,0.01,0.0046,0.0088,0.0059,0.0051,0.0071,0.0071,0.0088,0.0096,0.0072,0.0071,0.005,0.0071,0.008,0.0071,0.0077,0.0066,0.0068,0.0066,0.0075,0.0075,0.006,0.006]
	
	Dates = [619, 620, 623, 624, 625, 626, 627, 630, 701, 702, 703, 707, 708, 709, 710, 711, 714, 715, 716, 717, 718, 722, 723, 724, 725, 728, 729, 730, 731, 801, 804, 805, 806, 807, 808, 811, 812, 813, 814, 815, 818, 819, 820, 821, 822, 825, 826, 827, 828, 829, 902, 903, 904, 905, 908, 909, 910, 911, 912, 915, 916, 917, 918, 919]

	print "Conoco: "
	stock_function(Conoco, Dates)
	print "Apple "
	stock_function(Apple, Dates)
	print "Copw "
	stock_function(Copw, Dates)
