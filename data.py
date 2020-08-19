def data():
    groups = [
            {
                "type": "Jounglings",
                "id": "jounglings",
                "members": ["Mike", "Loren", "jan"],
                "schedule": ["06.06.2020 20:00", "10.06.2020 20:00"],
                "hw": ["first title", "second title"]
            },
            {
                "type": "Padawans",
                "id": "padawans",
                "members": ["PD Mike", " PD Loren", "PD Jan"],
                "schedule": ["06.06.2020 15:00", "10.06.2020 15:00"],
                "hw": ["PD first title", "PD second title"]
            }
        ]

    for group in groups:
        with open(f"src/{group['type'].lower()}/schedule.txt", "r") as f:
            for line in f.readlines():
                group["schedule"].append(line)

        with open(f"src/{group['type'].lower()}/studnets.txt", "r") as f:
            for line in f.readlines():
                group["members"].append(line)

        groups[groups.index(group)] = group

    return groups

def parse_homework():
    hw = {
        "jounglings": {
            "first title": "cartesian-optional.png",
            "second title": "cartesian-ptI.png",
            },
        "padawans": {
            "PD first title": "op1.png",
            "PD second title": "op2.png"
        }
    }

    return hw