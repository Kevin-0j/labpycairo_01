import cairo
import math
import os

# Set up the surface and context
WIDTH, HEIGHT = 600, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Background color (white)
context.set_source_rgb(1, 1, 1)
context.paint()

# 1. Draw the house base (rectangle)
context.set_source_rgb(0, 0, 1)  # Blue outline
context.set_line_width(2)
context.rectangle(150, 200, 300, 150)
context.stroke()

# 2. Draw the dome (semi-circle)
context.arc(300, 200, 100, math.pi, 0)
context.stroke()

# 3. Draw the door (rectangle)
context.set_source_rgb(0, 1, 0)  # Green outline
context.rectangle(275, 250, 50, 100)
context.stroke()

# 4. Draw the door knob (circle)
context.set_source_rgb(0, 0, 1)  # Blue fill
context.arc(320, 315, 5, 0, 2 * math.pi)
context.fill()

# 5. Draw the windows (two squares with crossbars)

# Left window
context.set_source_rgb(0, 1, 0)  # Green outline for the window
context.rectangle(190, 250, 50, 50)
context.stroke()

# Change the color for the crossbars (e.g., red)
context.set_source_rgb(0, 0, 1)  # Red color for the crossbars

# Draw horizontal crossbar
context.move_to(190, 275)
context.line_to(240, 275)
context.stroke()

# Draw vertical crossbar
context.move_to(215, 250)
context.line_to(215, 300)
context.stroke()

# Right window
context.set_source_rgb(0, 1, 0)  # Green outline for the window
context.rectangle(360, 250, 50, 50)
context.stroke()

# Change the color for the crossbars (e.g., red)
context.set_source_rgb(0, 0, 1)  # Red color for the crossbars

context.move_to(360, 275)
context.line_to(410, 275)
context.stroke()

context.move_to(385, 250)
context.line_to(385, 300)
context.stroke()

# 6. Draw the crescent moon
context.set_source_rgb(1, 0.843, 0)  # Golden yellow color for the moon
context.arc(420, 60, 30, 0, 2 * math.pi)
context.fill()

# Create a smaller overlapping circle to form a crescent shape
context.set_source_rgb(1, 1, 1)
context.arc(430, 60, 25, 0, 2 * math.pi)
context.fill()

# Check if the directory exists; if not create it
if not os.path.exists('Output files'):
    os.makedirs('Output files')

# Save the drawing to a PNG file
surface.write_to_png("Output files/2D_house_drawing.png")