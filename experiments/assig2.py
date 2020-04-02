#1
Geometry Management
All Tkinter widgets have access to specific geometry management methods, which have the purpose of organizing widgets throughout the parent widget area. Tkinter exposes the following geometry manager classes: pack, grid, and place.

116.                The pack() Method -This geometry manager

                         organizes widgets in blocks before placing

                          them in the parent widget.

117.                 The grid() Method -This geometry

                          manager organizes widgets in a table-like structure in

                          the parent widget.

118.                 The place() Method -This geometry manager organizes

                          widgets by placing them in a specific position in the                                 

                            parent   widget.

Let us study the geometry management methods briefly:

pack()

This geometry manager organizes widgets in blocks before placing them in the parent widget.

Syntax

widget.pack( pack_options )

Here is the list of possible options:

119.                   expand: When set to true, widget expands to fill any

                           space not otherwise used in widget’s parent.

120.                   fill: Determines whether widget fills any extra space

                           allocated to it by the packer, or keeps its own minimal

                           dimensions: NONE (default), X (fill only horizontally),

                           Y (fill only vertically), or BOTH (fill both horizontally 

                            and vertically).

121.                   side: Determines which side of the parent widget 

                           packs against: TOP (default), BOTTOM, LEFT, or

                            RIGHT.

Example

Try the following example by moving cursor on different buttons:

from Tkinter import *

root = Tk()

frame = Frame(root)

frame.pack()

bottomframe = Frame(root)

bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text=”Red”, fg=”red”)

redbutton.pack( side = LEFT)

greenbutton = Button(frame, text=”Brown”, fg=”brown”)

greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text=”Blue”, fg=”blue”)

bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text=”Black”, fg=”black”)

blackbutton.pack( side = BOTTOM) root.mainloop()

Here is the list of possible options:

122.              column : The column to put widget in; default 0

                      (leftmost column).

123.               columnspan: How many columnswidgetoccupies;

                       default 1.

124.               ipadx, ipady :How many pixels to pad widget,

                       horizontally and vertically, inside widget’sborders.

125.                padx, pady : How many pixels to pad widget,

                        horizontally and vertically, outside v’s borders.

126.               row: The row to put widget in; default the firstrow that

                         is still empty.

127.               rowspan : How many rowswidget occupies;default 1.

128.               sticky : What to do if the cell is larger than widget.

                        By default,with sticky=”, widget is centered in its cell.

                         sticky may be the string concatenation of zero or more

                         of N, E, S, W, NE, NW, SE, and SW, compass directions

                          indicating the sides and corners of the cell to which

                          widget sticks.

Example

Try the following example by moving cursor on different buttons:

import Tkinter

root = Tkinter.Tk( )

for r in range(3):

for c in range(4):

Tkinter.Label(root, text=’R%s/C%s’%(r,c),

borderwidth=1).grid(row=r,column=c)

root.mainloop( )

This would produce the following result displaying 12 labels arrayed in a 3 x 4 grid:

129.              3. place()

This geometry manager organizes widgets by   placing them in a

specific position in the parent widget.

Syntax

widget.place( place_options )

Here is the list of possible options:

130.               anchor : The exact spot of widget other options refer to:

                        may be N, E, S, W, NE, NW, SE, or SW, compass

                        directions indicating the corners and sides of widget;

                       default is NW (the upper left corner of widget)

131.               bordermode : INSIDE (the default) to indicate that other

                       options refer to the parent’s inside (ignoring the

                       parent’s border); OUTSIDE otherwise.

132.              height,  width : Height and width in pixels.

133.              relheight, relwidth : Height and width as a float between

                      0.0 and 1.0, as a fraction of the height and width of the

                      parent widget.

134.              relx, rely : Horizontal and vertical offset as a float

                       between 0.0 and 1.0, as a fraction of the height and

                         width of the parent widget.

135.              x, y : Horizontal and vertical offset in pixels.

Example

Try the following example by moving cursor on different buttons:

from Tkinter import *

import tkMessageBox

import Tkinter

top = Tkinter.Tk()

def helloCallBack():

tkMessageBox.showinfo( “Hello Python”, “Hello World”)

B = Tkinter.Button(top, text =”Hello”, command = helloCallBack)

B.pack()

B.place(bordermode=OUTSIDE, height=100, width=100)

top.mainloop()

When the above code is executed, it produces the following result:

#2
import Tkinter package and create a window and set its title

from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

To add a label to our previous example, we will create a label using the label class like this

lbl = Label(window, text="Hello")

Then we will set its position on the form using the grid function and give it the location like this

lbl.grid(column=0, row=0)

adding the button to the window, the button is created and added to the window the same as the label

btn = Button(window, text="Click Me")

btn.grid(column=1, row=0)

window.mainloop()

#3

import MySQLdb
from numpy.random import randint 

try:
    con=MySQLdb.connect('localhost','root','pw','db')

    c=con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS FIFA (scores int)"
    c.execute(sql)
    for i in range(1,100000):
        r=randint(low=10,high=30)
        c.execute('INSERT INTO FIFA VALUES(%s)',(r))

    con.close()

except:
    print("Error connecting db")


#--- 6.4126 seconds --- to save 100000 records in Database

from numpy.random import randint
f=open("events.txt","w+")
for i in range(1,100000):
    r=str(randint(low=10,high=30))
    f.write(r)

f.close()

#--- 1.0710008144378662 seconds --- to save 100000 records in text file

#4
#server
import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send(bytes('Thank you for connecting','utf8'))
    conn.close()
# client
import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
s.send(bytes("Hello server!",'utf8'))

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')