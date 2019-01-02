
def welcome():
    print(
        r" + + + + + + + + + + + + + + +" + "\n",
        r"+   ______  ___     __  __  +" + "\n",
        r"+  /_  __/ /   |   / / / /  +" + "\n",
        r"+   / /   / /| |  / / / /   +" + "\n",
        r"+  / /   /  _  | / /_/ /    +" + "\n",
        r"+ /_/   /_/  |_| \____/     +" + "\n",
        r"+                           +" + "\n",
        r"+ + + + + + + + + + + + + + +" + "\n\n",
        "Welcome to TAU - Helper for formatting music directory ",
        "and metadata on your PC.\n"
    )


def choose_work():

    print("""Select utility:
        0 - Scan music directory
        1 - Estimate new state
        2 - Update music directory with estimated state
        3 - Load flow from file
        x - Exit
    """)

    work = str(input("Select: "))

    try:
        work = int(work)
        return work
    except ValueError:
        pass
