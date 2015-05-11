from sys import argv
amphours = 12


def time_remaining(percent, amps):
    hours = (amphours * (percent / 100)) / amps
    return (hours * 3600)


def usage():
    print("timeremaining.py PERCENT(0-100) AMPS")

if __name__ == "__main__":
    if len(argv) < 3:
        usage()
    else:
        print(
            time_remaining(float(argv[1]), float(argv[2]))
        )
