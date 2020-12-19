import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv

df = pd.read_csv("data.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()


height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

print("The Mean, Median and Mode of height is {}, {}, and {} respectively".format(height_mean, height_median, height_mode))
print("The Mean, Median and Mode of weight is {}, {}, and {} respectively".format(weight_mean, weight_median, weight_mode))

height_std_deviation = statistics.stdev(height_list)
weight_std_deviation = statistics.stdev(weight_list)

height_first_std_deviation_start, height_first_std_deviation_end = height_mean-height_std_deviation, height_mean+height_std_deviation
height_second_std_deviation_start, height_second_std_deviation_end = height_mean-(2*height_std_deviation), height_mean+(2*height_std_deviation)
height_third_std_deviation_start, height_third_std_deviation_end = height_mean-(3*height_std_deviation), height_mean+(3*height_std_deviation)

weight_first_std_deviation_start, weight_first_std_deviation_end = weight_mean-weight_std_deviation, weight_mean+weight_std_deviation
weight_second_std_deviation_start, weight_second_std_deviation_end = weight_mean-(2*weight_std_deviation), weight_mean+(2*weight_std_deviation)
weight_third_std_deviation_start, weight_third_std_deviation_end = weight_mean-(3*weight_std_deviation), weight_mean+(3*weight_std_deviation)

height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]

weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result > weight_first_std_deviation_start and result < weight_first_std_deviation_end]
weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result > weight_second_std_deviation_start and result < weight_second_std_deviation_end]
weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result > weight_third_std_deviation_start and result < weight_third_std_deviation_end]

print("{}% of data for height lies within One standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within Two standard deviations".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within Three standard deviations".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))
print("{}% of data for weight lies within One standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within Two standard deviations".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within Three standard deviations".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))

fig = ff.create_distplot([height_list], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[height_mean, weight_mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[height_first_std_deviation_start, height_first_std_deviation_start], y=[0, 0.1], mode="lines", name="STANDARD DEVIATION Height 1"))
fig.add_trace(go.Scatter(x=[height_first_std_deviation_end, height_first_std_deviation_end], y=[0, 0.1], mode="lines", name="STANDARD DEVIATION Weight 1"))
fig.add_trace(go.Scatter(x=[weight_second_std_deviation_start, weight_second_std_deviation_start], y=[0, 0.1], mode="lines", name="STANDARD DEVIATION Height 2"))
fig.add_trace(go.Scatter(x=[weight_second_std_deviation_end, weight_second_std_deviation_end], y=[0, 0.1], mode="lines", name="STANDARD DEVIATION Weight 2"))
fig.show()
