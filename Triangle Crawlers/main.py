import random

possible_pos = ["A", "B", "C", "D"]
sim_count = 100


def run_sim():
    crawler_pos = "A"                                           # Sets initial location of crawler
    print(crawler_pos)
    last_pos = crawler_pos
    # TODO: Math part
    while crawler_pos != possible_pos[3]:
        new_pos = random.randint(0, 3)
        if (crawler_pos != possible_pos[3]                      # Makes sure the crawler is allowed
                and possible_pos[new_pos] != crawler_pos        # to move to the new position
                and possible_pos[new_pos] != last_pos):
            last_pos = crawler_pos
            crawler_pos = possible_pos[new_pos]
            print(crawler_pos)
        elif crawler_pos == last_pos:                           # Makes sure that the crawler doesn't
            new_pos = random.randint(0, 3)                      # move back to where it came from
            if (crawler_pos != possible_pos[3]
                    and possible_pos[new_pos] != crawler_pos
                    and possible_pos[new_pos] != last_pos):
                last_pos = crawler_pos
                crawler_pos = possible_pos[new_pos]
                print(crawler_pos)


for i in range(sim_count):                                      # Runs the simulation
    run_sim()
    print("\n")
