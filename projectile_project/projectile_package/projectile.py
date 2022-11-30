import matplotlib.pyplot as plt
from numpy import sign

def calculate_acceleration_y(v, k=0.0, mass=1.0, gravity=-9.81):
    '''
    Calculate the acceleration based on combined forces from gravity and 
    air resistance.
    Args:
        v (float) : 
            velocity (m/s) for this time step
        k (float) : 
            Combined air resistance coefficient, based on F=-kv^2. 
            Should be positive.
            Default = 0.0  i.e. no air resistance
        mass (float) : 
            Mass of the falling object. Needed if k > 0.
            Default = 1.0
        gravity (float) :
            Value for gravity to use when calculating gravitational force in m/s2.
            Default = -9.81
    Returns:
        float : accelaration calculated for this time step
    '''
    force_gravity = mass*gravity
    force_air = -sign(v)*k*v**2
    total_force = force_gravity + force_air
    a_y = total_force/mass
    
    return a_y

def calculate_acceleration_x(v, k=0.0, mass=1.0):
    '''
    Calculate the acceleration based on 
    air resistance.
    Args:
        v (float) : 
            velocity (m/s) for this time step
        k (float) : 
            Combined air resistance coefficient, based on F=-kv^2. 
            Should be positive.
            Default = 0.0  i.e. no air resistance
        mass (float) : 
            Mass of the falling object. Needed if k > 0.
            Default = 1.0
        gravity (float) :
            Value for gravity to use when calculating gravitational force in m/s2.
            Default = -9.81
    Returns:
        float : accelaration calculated for this time step
    '''
    
    force_air = -sign(v)*k*v**2
    total_force = force_air
    a_x = total_force/mass
    
    return a_x


def update_state(t, x, v, a, dt=0.1):
    '''
    Update each parameter for the next time step.
    Args:
        t, x, v, a (float) : 
            time (s), position (m) and velocity (m/s) and acceleration (m/s2) value for this time step.
        dt (float) :
            time interval (s) for this small time step
    Returns:
        float, float, float : Updated values for t, h, v after this time step
    '''
    distance_moved = v*dt + (1/2)*a*(dt**2)
    v += a*dt
    t += dt
    
    x += distance_moved
    
    return t, x, v


def flying_mass(initial_height, k=0.0, mass=1.0, dt=0.1):
    '''
    Model a falling mass from a given height.
    
    Args:
        initial_height (float) : 
            Starting height for the model in metres.
        k (float) :
            Combined air resistance coefficient, based on F=-kv^2. 
            Should be positive.
            Default = 0.0  i.e. no air resistance
        mass (float) :
            Mass of the object. Only needed if k is not 0.
            Default = 1.0  (kg)
        dt (float, optional) : 
            Time interval for each time step in seconds.
            Default = 0.1
    
    Returns:
        list, list, list : Three lists containing the time, height and velocity
    '''
    # Fixed input values
    start_x_velocity = 10.0 # m/s
    start_y_velocity = 10.0 # m/s
    gravity = -9.81 # m/s2

    # Initial values for our parameters
    x_distance_moved = 0
    h = initial_height
    v_x= start_x_velocity
    v_y = start_y_velocity
    t = 0.0
    

    # Create empty lists which we will update
    x_velocity = []
    y_velocity = []
    time = []
    x_distance = []
    height =[]

    # Keep looping while the object is still falling
    while h > 0:
        # Evaluate the state of the system - start by calculating the total force on the object
        a_y = calculate_acceleration_y(v, k=k, mass=mass, gravity=gravity)
        a_x = calculate_acceleration_x(v, k=k, mass=mass)

        # Append values to list and then update
        y_velocity.append(v_y)
        x_velocity.append(v_x)
        time.append(t)
        x_distance.append(x_distance_moved)
        height.append(h)

        # Update the state for time, height and velocity
        t, h, v = update_state(t, h, v_y, a_y, dt=dt)
        t, h, v = update_state(t, h, v_x, a_x, dt=dt)    
    
        return time,x_velocity, y_velocity, x_distance, height
    
    t, x, h, v_y, v_x = flying_mass(20, k=0.035)