import matplotlib.pyplot as pyplot

def make_plot(xs, ys):
    pyplot.plot(xs, ys)
    scale = 'log'
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('')
    pyplot.xlabel('n')
    pyplot.ylabel('run time (s)')
    pyplot.show()
