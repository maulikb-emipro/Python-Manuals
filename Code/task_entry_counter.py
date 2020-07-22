import math

spent_hours = int(input("Enter Spent Hours :- "))

spent_minutes = float(input("Enter Spent minutes :- "))

minutes_in_float = spent_minutes / 60
total_spent_time = float(spent_hours) + minutes_in_float

print("Total spent time : {0}".format(total_spent_time))

needed_task_entry_in_float = total_spent_time * 0.80

print("Needed entry in float : {0}".format(needed_task_entry_in_float))

needed_minutes_in_float = needed_task_entry_in_float - int(needed_task_entry_in_float)

needed_minutes = int(math.ceil(needed_minutes_in_float * 60))

print("Needed entry in Hours : {0}:{1}".format(int(needed_task_entry_in_float), needed_minutes))
