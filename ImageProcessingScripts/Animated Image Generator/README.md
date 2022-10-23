# Animated Image Generator

## Aim

This is a simple script to concatenate frame images, generating animation.

## Short description

- With all valid image files in ```--target``` directory, a single animated image will be generated and saved
  as ```--output```.
- Other valid options are:
    - ```--speed```: How long a single frame will be shown in resulting animation(in milliseconds).
    - ```--output_extension```: Instead of designating ```output``` option, one can simply set this to get
      results.{extension} file in original target directory.

## Workflow

- This script reads all valid image files using ```glob``` module.
    - Valid image files are files with ```IMG_EXTENSIONS```
    - Alpha channel will not be used, since it seems gif extension does not support it.
- Then, they are concatenated by ```Pillow.Image``` module.

## Setup instructions

- The only thing to setup is to install Pillow.

```
pip install -r requirements.txt
```

## Output

- Script
```
$ python animated_image_generator.py --target "./images" --output_extension "gif" --speed 25
```
- Result
![output_gif](images/result.gif)

