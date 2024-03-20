# make the dictionary for activities and time spent during an average day
student_activities={"sleeping":8, "classes":6, "studying":3.5, "TV":2, "Music":1,}
# calculate 'other' category
student_activities['Other'] = 24 - sum(student_activities.values())
print(student_activities)
#create a variable of the requested activity that can be modified
student_activities_modified='sleeping'
print(student_activities[student_activities_modified])

# import pyplot function from matplotlib
import matplotlib.pyplot as plt
# name the labels
activities = list(student_activities.keys())
# input the value of each part of the pie chart
times = list(student_activities.values())
# create the pie chart
plt.figure()
plt.pie(times,labels=activities,autopct='%1.1f%%', shadow=False, startangle=90)
plt.title("The average day of a university student")
# equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')
# show the pie chart
plt.show()
# close the pie chart
plt.clf