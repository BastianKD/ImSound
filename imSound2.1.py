# pip install pillow
# pip install pygame

from PIL import Image, ImageStat
import sys, time, pygame


# tracks

lead = {"r": "Music/red_trio.wav",
        "g": "Music/piano_green.wav",
        "b": "Music/guitars_blue.wav",
        "b&w": "Music/organ_red.wav"}
bass = {"low": "Music/beat_red.wav",
        "mid": "Music/beat_green.wav",
        "high": "Music/beat_blue.wav"}
drums = {"low": "Music/drums_red.wav",
         "mid": "Music/drums_green.wav",
         "high": "Music/drums_blue.wav"}


# imagedata

def statistics(img):
    stat = ImageStat.Stat(img)
    r, g, b = stat.mean
    print "Average color: rgb(%d, %d, %d)" % (r, g, b)
    if r > g and r > b:
        dominant_color = "r"
    elif g > r and g > b:
        dominant_color = "g"
    elif b > r and b > g:
        dominant_color = "b"
    else:
        dominant_color = "b&w"

    brightness = ((0.2126 * r) + (0.7152 * g) + (0.0722 * b))/255.0
    print("Brightness:", brightness)
    if brightness > 0.33:
        brightness = "low"
    elif 0.33 >= brightness > 0.66:
        brightness = "mid"
    else:
        brightness = "high"

    r, g, b = stat.stddev
    contrast = ((0.2126 * r) + (0.7152 * g) + (0.0722 * b))/255.0
    print("Contrast:", contrast)
    if contrast > 0.12:
        contrast = "low"
    elif 0.12 >= contrast > 0.24:
        contrast = "mid"
    else:
        contrast = "high"

    return([dominant_color, brightness, contrast])

# playthemusic

def start_music(im_data):
    pygame.init()

    SoundB1 = pygame.mixer.Sound(lead[im_data[0]])
    SoundB2 = pygame.mixer.Sound(drums[im_data[1]])
    SoundB3 = pygame.mixer.Sound(bass[im_data[2]])

    psound = SoundB1.play()
    SoundB2.play()
    SoundB3.play()
    while psound.get_busy():
        time.sleep(1)


# launchtheprogram

def main():
    print("Welcome to imSound!\nJust give me a path to a picture and I'll give you the sound to it!")
    filename = raw_input("\tFile: ")
    try:
        img = Image.open(filename)
    except:
        print("I can't find any picture with this name!")
        sys.exit(0)
    if img.format != "JPEG":
        print("Sorry I need some JPEG!")
        sys.exit(0)

    # resize the image to reduce processing time
    img.thumbnail((200,200))
    im_data = statistics(img)
    img.close()
    start_music(im_data)


if __name__ == "__main__":
    main()
