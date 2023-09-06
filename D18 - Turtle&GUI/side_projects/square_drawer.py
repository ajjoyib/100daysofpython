def sq_drawer(obj, size):
    obj.fd(size)
    obj.lt(90)
    obj.fd(size)
    obj.lt(90)
    obj.fd(size)
    obj.lt(90)
    obj.fd(size)


def draw_dash_line(obj, dash_length, n_dashes):
    for a in range(n_dashes):
        obj.fd(dash_length)
        obj.pu()
        obj.fd(dash_length)
        obj.pd()


def draw_dotted_sq(obj, dash_length, size):
    for a in range(size):
        obj.fd(dash_length)
        obj.pu()
        obj.fd(dash_length)
        obj.pd()
        # obj.right(90)

