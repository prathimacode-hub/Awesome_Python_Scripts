import argparse
import os
from glob import glob

from PIL import Image

IMG_EXTENSIONS = ['jpg', 'jpeg', 'png']  # Supported Image Extensions
OUTPUT_EXTENSIONS = ['gif', 'webp', 'png']  # Supported Animated Image Extensions

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('--target', help='Target directory which contains frame images.')
parser.add_argument('--output_extension', default='gif',
                    help='Output file extension. GIF(default), WEBP or APNG(animated png).')
parser.add_argument('--speed', default=25, type=int, help='Milliseconds per frame. Smaller means faster.')
parser.add_argument('--output', default=None, help='Output file name. This overrides `format` argument.')

args = parser.parse_args() # parse all args.

# Find all valid image files.
frames = []
for ext in IMG_EXTENSIONS:
    frames.extend(glob(os.path.join(args.target, f'*.{ext}')))

# Open all images
frames = [Image.open(path).convert('RGB') for path in frames]
print(f'{len(frames)} files found')

# Save as an animation
output_path = os.path.join(args.target, f"result.{args.output_extension}")
if args.output is not None:
    output_path = args.output


frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0,
               duration=args.speed)
print(f'Save success for {output_path}')
