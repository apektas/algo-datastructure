import time
def countDown(n):
    # base case
    if n <0: return
    print(n)
    time.sleep(1)
    countDown(n-1)

countDown(5)