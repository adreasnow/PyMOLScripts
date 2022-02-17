# axes.py
from pymol.cgo import *
from pymol import cmd
from pymol.vfont import plain

# create the axes object, draw axes with cylinders coloured red, green,
#blue for X, Y and Z
def axes(length=3.0,width=0.05,letter_thickness=0.03,text_size=0.5,conelength=0.3,coneradius=0.1,color="ffffff"):
   def hex2rgb(hex):
      r = (int(hex[0:2], 16))/255
      g = (int(hex[2:4], 16))/255
      b = (int(hex[4:6], 16))/255
      return([r, g, b])
   color=hex2rgb(color)
   col_r = color[0]
   col_g = color[1]
   col_b = color[2]

   obj = [
      CYLINDER, 0., 0., 0., length, 0., 0., width, col_r, col_g, col_b, col_r, col_g, col_b,
      CYLINDER, 0., 0., 0., 0., length, 0., width, col_r, col_g, col_b, col_r, col_g, col_b,
      CYLINDER, 0., 0., 0., 0., 0., length, width, col_r, col_g, col_b, col_r, col_g, col_b,
      CONE, length, 0., 0., length+conelength, 0., 0., coneradius, 0.0, col_r, col_g, col_b, col_r, col_g, col_b, 1.0, 0.0,
      CONE, 0., length, 0., 0., length+conelength, 0., coneradius, 0.0, col_r, col_g, col_b, col_r, col_g, col_b, 1.0, 0.0,
      CONE, 0., 0., length, 0., 0., length+conelength, coneradius, 0.0, col_r, col_g, col_b, col_r, col_g, col_b, 1.0, 0.0,
      ]

   # add labels to axes object (requires pymol version 0.8 or greater, I
   # believe

   # cyl_text(obj,plain,[-5.,-5.,-1],'Origin',0.20,axes=[[3,0,0],[0,3,0],[0,0,3]])
   cyl_text(obj,plain,[length+(2*conelength),0.,0.],'X',letter_thickness,axes=[[text_size,0,0],[0,text_size,0],[0,0,text_size]],color=color)
   cyl_text(obj,plain,[0.,length+(2*conelength),0.],'Y',letter_thickness,axes=[[text_size,0,0],[0,text_size,0],[0,0,text_size]],color=color)
   cyl_text(obj,plain,[0.,0.,length+(2*conelength)],'Z',letter_thickness,axes=[[text_size,0,0],[0,text_size,0],[0,0,text_size]],color=color)

   # then we load it into PyMOL
   cmd.load_cgo(obj,'axes')
   cmd.reset()