#!/usr/bin/env python

"""Example: Declaring Expressions and Retrieving Subgradients"""

from spy import *
if __name__ == "__main__":
    x = var('x')
    y = var('y')
    
    ex = x+3
    print ex
    ex = 3+x
    print ex
    
    ex = exp(x+y)
    print ex.get_vars()
    print ex.get_value()
    print ex.get_value({'x': 2, 'y': -1})
    print ex.get_value({'x': 2})
    
    ex = exp(x)
    print ex
    print 'computing subgrad at x=2, y=-1'
    print ex.subgrad({'x': 2, 'y': -1})
    
    ex = exp(exp(x))
    print ex
    print ex.get_value({'x': 1})
    print ex.get_value({'x': 0})
    print ex.subgrad({'x': 0})
    
    ex = max(x, y)
    print ex
    print ex.get_value({'x': 1124, 'y': 233})
    print ex.subgrad({'x': 1124, 'y': 233})
    
    ex = 3*x+y*4
    print ex
    print ex.get_value({'x': 1124, 'y': 233})
    print ex.subgrad({'x': 1124, 'y': 233})
    
    ex = sqrt(x+y)
    print ex
    print ex.get_value({'x': 3, 'y': 4})
    print ex.supergrad({'x': 3, 'y': 4})

    ex = max(0, 3*x)
    print ex
    print ex.subgrad({'x': 123})
    
    ex = 3*x
    print ex
    print ex.subgrad({'x': 123})
	
    ex = abs(x-3)+exp(x)
    print ex
    print ex.subgrad({'y': -2})
    
    ex = abs(-3+x-3)+exp(x)
    print ex
    print ex.subgrad({'y': -2})
    
    ex = x+3
    print ex
    print ex.get_value({'x': 12345})
    print ex.subgrad({'x': 12345})

    ex = geo_mean(x,y)
    print ex
    print ex.get_value({'x':2,'y':8})
    print ex.subgrad({'x':1,'y':100})

    ex = square_pos(x)
    print ex.get_value({'x':2})
    print ex.get_value({'x':-5})
    print ex.subgrad({'x':1})
    
    ex = rel_entr(x,y)
    print ex
    print ex.get_value({'x':2.0,'y':8.0})
    print ex.subgrad({'x':1,'y':100})

    ex = pow_pos(x,5.0)
    print ex
    print ex.get_value({'x': 2.0})
    print ex.get_value({'x': -2.0})
    print ex.subgrad({'x':2.0})
