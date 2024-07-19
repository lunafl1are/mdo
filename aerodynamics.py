from math import pi
def mixed_wing_area(c_r, c_t, b_rect, b_trap):
  """
  Computes the area for a mixed wing (trapezoidal + rectangular)
  >>> mixed_wing_area(2,2,4,5)
  18.0
  """
  s = c_r * b_rect + (c_r + c_t) * b_trap/2
  return s

def trapezoidal_wing_area(c_r, c_t, b):
  """
  Computes the area for a trapezoidal wing
  >>> trapezoidal_wing_area(0.5,0.2,2)
  0.7
  """
  return (c_r + c_t) * b / 2
  

def eliptical_wing_area(c_r, b):
  """
  Computes the area for a trapezoidal wing
  >>> eliptical_wing_area(0.4, 2)
  0.6283185307179586
  """
  return pi/4 * b * c_r


def taper_ratio(b_rect, b_trap, c_t, c_r):
  """
  >>> taper_ratio(4,2,2,1)
  1.5
  """
  
  if(b_rect>0 and b_trap >0):
    afil = (1 + c_t / c_r)/2 #entender
  else:
    afil = c_t / c_r
  return afil

def wingspan(b_rect, b_trap):
  """
  >>> wingspan(2,4)
  6
  """

  b = b_rect + b_trap
  return b

def aspect_ratio(b, S):
  """
  >>> aspect_ratio (2,4)
  1.0
  """

  return b**2 / S

def lift(rho, v, S, C_l):
  """
  >>> lift(1.225, 17, 0.78, 1.2)
  165.68370000000002
  """

  return rho * v**2 * S * C_l / 2

if __name__ == "__main__":
  c_r, c_t, b_rect, b_trap = 0.455, 0.455, 2.35, 0
  print("When the inputs are:")
  print(f'c_r = {c_r} \nc_t = {c_t} \nb_rect = {b_rect} \nb_trap = {b_trap}\n')

  b = wingspan(b_rect, b_trap)
  s = mixed_wing_area(c_r, c_t, b_rect, b_trap)
  afil = taper_ratio(b_rect, b_trap, c_t, c_r)
  ar = aspect_ratio(b, s)

  results = {
    "Area": s,
    "Taper ratio": afil,
    "Wingspan": b,
    "Aspect ratio": ar,
  }
  print("The results are:")
  for key, value in results.items():
      print(f'{key} = {value}')