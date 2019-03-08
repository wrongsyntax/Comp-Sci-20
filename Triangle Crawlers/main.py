import random

possible_pos = ["A", "B", "C", "D"]
original_sim_count = int(input("How many crawlers would you like to simulate? "))
sim_count = original_sim_count
averages = []


def estimate_time(num):
    if num >= 100000:
        estimate = num / 100000 + 1
        print("The simulation should take approximately {} seconds.".format(estimate))
    else:
        print("The simulation should take less than a second.")


def run_sim():
    crawler_pos = possible_pos[0]
    last_pos = crawler_pos
    age = 1
    age_list = [1]

    while crawler_pos != possible_pos[3]:
        new_pos = random.randint(0, 3)
        if crawler_pos != new_pos and crawler_pos != last_pos:
            # Stores the crawler position for later before moving it
            last_pos = crawler_pos
            # Move the crawler
            crawler_pos = possible_pos[new_pos]
            age += 1
            age_list.append(age)
        elif crawler_pos == last_pos:
            last_pos = crawler_pos
            crawler_pos = possible_pos[new_pos]
            age += 1
            age_list.append(age)

    average = sum(age_list) / len(age_list)
    return average


estimate_time(sim_count)
print("Running simulation...")

while sim_count != 0:
    averages.append(run_sim())
    sim_count -= 1

print("Simulation complete.")
# Calculate and find the values needed
total_average = sum(averages) / len(averages)
youngest = min(averages)
oldest = max(averages)
print("The total average lifespan of {} crawlers is {} days.".format(original_sim_count, total_average))
print("The youngest crawler to die was {} days old. The oldest to die was {} days old.".format(youngest, oldest))
