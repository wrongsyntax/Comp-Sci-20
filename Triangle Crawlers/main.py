import random

possible_pos = ["A", "B", "C", "D"]
sim_count = 1


def run_sim():
    crawler_pos = "A"
    last_pos = crawler_pos
    while crawler_pos != possible_pos[3]:
        new_pos = random.randint(0, 3)
        if (crawler_pos != possible_pos[3]
                and possible_pos[new_pos] != crawler_pos
                and possible_pos[new_pos] != last_pos):
            last_pos = crawler_pos
            # print("Last: " + last_pos)
            crawler_pos = possible_pos[new_pos]
            print(crawler_pos)
        elif crawler_pos == last_pos:
            new_pos = random.randint(0, 3)
            if (crawler_pos != possible_pos[3]
                    and possible_pos[new_pos] != crawler_pos
                    and possible_pos[new_pos] != last_pos):
                last_pos = crawler_pos
                # print("Last: " + last_pos)
                crawler_pos = possible_pos[new_pos]

                print(crawler_pos)


for i in range(sim_count):
    run_sim()
    print("\n")
