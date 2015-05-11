percent_voltage = [
    (100, 12.73),
    (90, 12.62),
    (80, 12.50),
    (70, 12.37),
    (60, 12.24),
    (50, 12.10),
    (40, 11.96),
    (30, 11.81),
    (20, 11.66),
    (10, 11.51)
]
derived_percents = []
for i in range(len(percent_voltage)):
    if i+1 < len(percent_voltage):
        v0 = percent_voltage[i][1]
        v1 = percent_voltage[i+1][1]
        percent = percent_voltage[i][0]
        step = (v0-v1) / 10
        for i in range(10):
            derived_percents.append(
                (
                    round(
                        v0 - (step * i),
                        3
                    ),
                    percent - i
                )
            )
print(derived_percents)
