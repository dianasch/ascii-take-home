"""Functions to create ASCII art.

Coordinates for start_x and start_y are the top left of the rectangle
and end_x and end_y are bottom right of the rectangle."""


class Canvas:
    """Canvas object."""

    def __init__(self):
        self.rows = 10
        self.columns = 10
        self.canvas = [[" " for i in range(self.columns)] for i in range(self.rows)]

    def render_canvas(self):
        """Print canvas out row by row."""

        for row in self.canvas:
            print(" ".join(row))

    def clear_canvas(self):
        """Clear all shapes from canvas."""

        for i in range(self.columns):

            self.canvas[i] = [" "] * self.rows

    def add_rectangle(self, rectangle):
        """Add a rectangle shape to canvas."""

        # Validate input to make sure original rectangle fits on canvas
        if rectangle.start_x < 0 or\
            rectangle.end_x > self.columns - 1 or\
            rectangle.start_y < 0 or\
            rectangle.end_y > self.columns - 1:

            return "Oops! Please plot a rectangle that fits on the canvas."

        # Loop through rows in canvas
        for i, row in enumerate(self.canvas):

            # If rows are between start_y and end_y
            if rectangle.start_y <= i <= rectangle.end_y:

                # Change values between start_x and start_y to fill_char
                row[rectangle.start_x:(rectangle.end_x + 1)] = [rectangle.fill_char] * (rectangle.end_x - rectangle.start_x + 1)

    def change_rectangle_fill(self, rectangle, char):
        """Change a rectangle fill's character."""

        # If you reassign fill_char, you have to readd rectangle to canvas
        # Better to replot rectangle
        # rectangle.fill_char = char

        # Replot same rectangle with char instead of fill_char
        for i, row in enumerate(self.canvas):

            if rectangle.start_y <= i <= rectangle.end_y:

                row[rectangle.start_x:(rectangle.end_x + 1)] = [char] * (rectangle.end_x - rectangle.start_x + 1)
    
    def translate_rectangle(self, rectangle, axis, num):

        # If translation is on the x axis
        if axis == "x":

            # Increment start_x and end_x by num
            rectangle.start_x += num
            rectangle.end_x += num

            # If rectangle is shifted to the left off canvas, but right edge still on canvas
            if rectangle.start_x < 0 and rectangle.end_x <= self.columns - 1:

                # Loop through rows in canvas
                for i, row in enumerate(self.canvas):

                    # If rows are between start_y and end_y
                    if (self.rows - rectangle.end_y - 1) <= i <= (self.rows - rectangle.start_y - 1):

                        # Plot rectangle up to end_x with fill_char
                        row[:rectangle.end_x + 1] = [rectangle.fill_char] * rectangle.end_x

                        # Reset values greater than end_x with blank space
                        row[rectangle.end_x + 1:] = [" "] * (self.columns - rectangle.end_x - 1)

            # If rectangle is shifted to the right off canvas, but left edge still on canvas
            elif rectangle.end_x > self.columns - 1 and rectangle.start_x >= 0:

                # Loop through rows in canvas
                for i, row in enumerate(self.canvas):

                    # If rows are between start_y and end_y
                    if (self.rows - rectangle.end_y - 1) <= i <= (self.rows - rectangle.start_y - 1):

                        # Plot rectangle from start_x to end of canvas with fill_char
                        row[rectangle.start_x:] = [rectangle.fill_char] * (self.columns - rectangle.start_x)

                        # Reset values less than start_x with blank space
                        row[:rectangle.start_x] = [" "] * rectangle.start_x

            # Original rectangle is validated -- moot edge case
            # If rectangle is shifted and is wider than canvas
            # elif rectangle.start_x < 0 and rectangle.end_x > self.columns - 1:

            #     # Loop through rows in canvas
            #     for i, row in enumerate(self.canvas):

            #         # If rows are between start_y and end_y
            #         if (self.rows - rectangle.end_y - 1) <= i <= (self.rows - rectangle.start_y - 1):

            #             # Fill entire row with fill_char
            #             self.canvas[i] = [rectangle.fill_char] * self.rows

            # Otherwise, width of rectangle fits neatly inside width of canvas
            else:

                # Loop through rows in canvas
                for i, row in enumerate(self.canvas):

                    # If rows are between start_y and end_y
                    if rectangle.start_y <= i <= rectangle.end_y:

                        # If num is positive
                        if num > 0:

                            # Reset values smaller than start_x to a blank space
                            row[:rectangle.start_x] = [" "] * rectangle.start_x

                            # Plot the width of rectangle with fill_char
                            row[rectangle.start_x:(rectangle.end_x + 1)] = [rectangle.fill_char] * (rectangle.end_x - rectangle.start_x + 1)

                        # If num is negative
                        elif num < 0:

                            # Reset values greater than end_x to a blank space
                            row[rectangle.end_x:] = [" "] * (self.columns - rectangle.end_x)

                            # Plot the width of rectangle with fill_char
                            row[rectangle.start_x:(rectangle.end_x + 1)] = [rectangle.fill_char] * (rectangle.end_x - rectangle.start_x + 1)
                            
        # If translation is on the y axis
        elif axis == "y":

            # Increment start_y and end_y by num
            rectangle.start_y += num
            rectangle.end_y += num

            # If rectangle is shifted up off canvas, but bottom edge still on canvas
            if rectangle.start_y <= self.rows - 1 and rectangle.end_y <= 0:

                # Loop through rows in canvas
                for i, row in enumerate(self.canvas):

                    # If rows are less than or equal to bottom edge of rectangle
                    if i <= rectangle.end_y:

                        # Plot the width of rectangle with fill_char
                        row[rectangle.start_x:(rectangle.end_x + 1)] = [rectangle.fill_char] * (rectangle.end_x - rectangle.start_x + 1)

                    else:

                        # Reset other rows to blank spaces
                        self.canvas[i] = [" "] * self.columns

            # If rectangle is shifted down off canvas, but top edge still on canvas
            elif rectangle.start_y > self.rows - 1 and rectangle.end_y <= self.rows - 1:

                # Loop through rows in canvas
                for i, row in enumerate(self.canvas):

                    # If rows are greater than or equal to top edge of rectangle
                    if i >= rectangle.start_y:

                        # Plot the width of rectangle with fill_char
                        row[rectangle.start_x:(rectangle.end_x + 1)] = [rectangle.fill_char] * (rectangle.end_x - rectangle.start_x + 1)

                    else:

                        # Reset other rows to blank spaces
                        self.canvas[i] = [" "] * self.columns

            # Original rectangle is validated -- moot edge case
            # If rectangle is shifted and is taller than canvas
            # elif rectangle.start_y <= self.rows - 1 and rectangle.end_y <= 0:

            #     # Loop through all rows in canvas
            #     for i, row in enumerate(self.canvas):

            #         # Plot the width of rectangle with fill_char
            #         row[rectangle.start_x:(rectangle.end_x + 1)] = [rectangle.fill_char] * (rectangle.end_x - rectangle.start_x + 1)

            # Otherwise, height of rectangle fits neatly inside width of canvas
            else:

                # Loop through rows in canvas
                for i, row in enumerate(self.canvas):

                    # If rows are between start_y and end_y
                    if (self.rows - rectangle.end_y - 1) <= i <= (self.rows - rectangle.start_y - 1):

                        # Plot the width of rectangle with fill_char
                        row[rectangle.start_x:(rectangle.end_x + 1)] = [rectangle.fill_char] * (rectangle.end_x - rectangle.start_x + 1)
                    
                    else:

                        # Reset other rows to blank spaces
                        self.canvas[i] = [" "] * self.columns


class Rectangle:
    """Rectangle object."""

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char
