def countup():
    x = 1
    while True:
        yield x
        x += 1

if __name__=="__main__":
    c = countup()
    while True:
        print('time {}'.format(next(countup)))

