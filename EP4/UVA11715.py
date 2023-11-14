

# V = V0 + a*t
def get_acceleration(initial_speed, final_speed, time):
    acceleration = (final_speed - initial_speed) / time
    return acceleration


def get_final_speed(initial_speed, acceleration, time):
    final_speed = initial_speed + acceleration * time
    return final_speed


def get_initial_speed(final_speed, acceleration, time):
    initial_speed = final_speed - acceleration * time
    return initial_speed


def get_time(initial_speed, final_speed, acceleration):
    time = (final_speed - initial_speed) / acceleration
    return time


# S = S0 + V0*t + 1/2*a*t^2
def get_displacement(initial_speed, final_speed, time):
    displacement = initial_speed * time\
        + (get_acceleration(initial_speed, final_speed, time) * (time ** 2)) / 2
    return displacement


# V^2 = V0^2 + 2*a*S

def torricelli_final_speed(initial_speed, final_speed, displacement):
    final_speed = (initial_speed ** 2 + 2 *
                   acceleration * displacement) ** (1/2)
    return final_speed


def torricelli_initial_speed(acceleration, final_speed, displacement):
    initial_speed = (final_speed ** 2 - 2 *
                     acceleration * displacement) ** (1/2)
    return initial_speed


count = 1
while True:
    try:
        line = input().strip().replace("\n", "")
        line = line.split(" ")
        line = [float(i) for i in line]
        if line[0] == 0:
            break
        if line[0] == 1:
            initial_speed = line[1]
            final_speed = line[2]
            time = line[3]
            displacement = get_displacement(initial_speed, final_speed, time)
            acceleration = get_acceleration(initial_speed, final_speed, time)
            print(f"Case {count}: {displacement:.3f} {acceleration:.3f}")

        elif line[0] == 2:
            initial_speed = line[1]
            final_speed = line[2]
            acceleration = line[3]
            time = get_time(initial_speed, final_speed, acceleration)
            displacement = get_displacement(initial_speed, final_speed, time)
            print(f"Case {count}: {displacement:.3f} {time:.3f}")

        elif line[0] == 3:
            initial_speed = line[1]
            acceleration = line[2]
            displacement = line[3]
            final_speed = torricelli_final_speed(
                initial_speed, final_speed, displacement)
            time = get_time(initial_speed, final_speed, acceleration)
            print(f"Case {count}: {final_speed:.3f} {time:.3f}")

        else:
            final_speed = line[1]
            acceleration = line[2]
            displacement = line[3]
            initial_speed = torricelli_initial_speed(
                acceleration, final_speed, displacement
            )
            time = get_time(initial_speed, final_speed, acceleration)
            print(f"Case {count}: {initial_speed:.3f} {time:.3f}")

        count += 1
    except EOFError:
        break
