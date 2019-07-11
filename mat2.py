#!/usr/bin/python
def cal(x,y,z):
  if x=='add':
      return y+z
  elif x=='subtract':
      return y-z
  elif x=='divide':
    return y/z
  
  elif x=='multiple':
      return y*z
  else:
      print("input invalid")