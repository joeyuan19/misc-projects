from PIL import Image



def graph(f,                    # function to resolve
        x_min,                  # starting x value
        x_max,                  # ending x value (exclusive)
        img=None,               # image to graph on, Creates a new image if None
        width=500,              # Image width, is overridden if img is not None
        height=500,             # Image height, is overridden if img is noe None
        step_size=None,         # step size on which to evauluate f
        mesh_graph=False,       # replace existing Pixels (False), or average the color value (True)
        color=(0,0,0),          # graph color
        bg_color=(255,255,255), # graph background color, is only used on new images
        img_type = "RGB"        # image type
        ):
    """ Draw the graph of a function onto or into an image"""
    # Set the X Range
    x_range = x_max - x_min
    # Check if there is a provided step_size
    if step_size is None:
        step_size = float(x_range)/(width*2)
    else:
        step_size = float(step_size)
    # assert that values are floats
    x_min = float(x_min)
    x_max = float(x_max)
    # initialization before calculated graph
    x = x_min
    graph = []
    y_min = y_max = f(x_min)
    while x < x_max:
        y = f(x)
        y_min = min(y,y_min)
        y_max = max(y,y_max)
        graph.append((x,y))
        x += step_size
    if img is not None:
        width,height = img.size
    else:
        img = Image.new(img_type,(width,height),bg_color)

    y_range = y_max - y_min

    scaled_graph = []
    for point in graph:
        adj_x = int((width - 1) * ( (point[0] - x_min) / x_range ) )
        adj_y = (height-1) - int( (height-1) * ((point[1] - y_min)/y_range) )
        scaled_graph.append((adj_x,adj_y))

    im = img.load()
    for point in scaled_graph:
        im[point] = color

    return img

def graph_parametric(f_x,       # function to resolve x values
        f_y,                    # function to resolve y values
        t_min,                  # starting t value
        t_max,                  # ending t value (exclusive)
        img=None,               # image to graph on, Creates a new image if None
        width=500,              # Image width, is overridden if img is not None
        height=500,             # Image height, is overridden if img is noe None
        step_size=None,         # step size on which to evauluate f
        mesh_graph=False,       # replace existing Pixels (False), or average the color value (True)
        color=(0,0,0),          # graph color
        bg_color=(255,255,255), # graph background color, is only used on new images
        img_type = "RGB"        # image type
        ):
    """ Draw the graph of a function onto or into an image"""
    # Set the X Range
    t_range = t_max - t_min
    # Check if there is a provided step_size
    if step_size is None:
        step_size = float(t_range)/(width*2)
    else:
        step_size = float(step_size)
    # assert that values are floats
    t_min = float(t_min)
    t_max = float(t_max)
    # initialization before calculated graph
    t = t_min
    graph = []
    x_min = x_max = f_y(t_min)
    y_min = y_max = f_x(t_min)
    while t < t_max:
        x = f_x(t)
        y = f_y(t)
        x_min = min(x,x_min)
        x_max = max(x,x_max)
        y_min = min(y,y_min)
        y_max = max(y,y_max)
        graph.append((x,y))
        t += step_size
    if img is not None:
        width,height = img.size
    else:
        img = Image.new(img_type,(width,height),bg_color)

    x_range = x_max - x_min
    y_range = y_max - y_min

    scaled_graph = []
    for point in graph:
        adj_x = int( (width-1) * ((point[0] - x_min)/x_range) )
        adj_y = (height-1) - int( (height-1) * ((point[1] - y_min)/y_range) )
        scaled_graph.append((adj_x,adj_y))

    im = img.load()
    for point in scaled_graph:
        im[point] = color

    return img
