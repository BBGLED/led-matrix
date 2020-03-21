#!/usr/bin/env python

from samplebase import SampleBase

import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)

    def run(self):
        # Main function
        if __name__ == "__main__":
            run_text = RunText()
            if (not run_text.process()):
                run_text.print_help()

        if len(sys.argv) < 2:
            sys.exit("Require an image argument")
        else:
            image_file = sys.argv[1]

        image = Image.open(image_file)

        # Make image fit our screen.
        image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

        matrix.SetImage(image.convert('RGB'))

        try:
            print("Press CTRL-C to stop.")
            while True:
                time.sleep(100)
        except KeyboardInterrupt:
            sys.exit(0)

# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()

