import time
from progress.bar import Bar


def consoleProgressBar(total = 100):
    bar = Bar("Status: ", max=total)

    for i in range(total):
        time.sleep(0.1)
        bar.next()
    
    bar.finish()