import python_avatars as pa

#customising avtaar as per requirement
pa.Avatar(
    #selecting the back ground shape
    style=pa.AvatarStyle.CIRCLE,
    #selecting the face parts
    eyebrows=pa.EyebrowType.DEFAULT_NATURAL,
    eyes=pa.EyeType.HEART,
    nose=pa.NoseType.DEFAULT,
    mouth=pa.MouthType.EATING,
    facial_hair=pa.FacialHairType.NONE,
    #selecting bg shape colour
    background_color='#FF00FF',
    # Choose graphic shirt
    clothing=pa.ClothingType.GRAPHIC_SHIRT,
    clothing_color=pa.ClothingColor.GRAY_02,
    # Important to choose this as shirt_graphic, otherwise shirt_text will be ignored
    shirt_graphic=pa.ClothingGraphic.CUSTOM_TEXT,
    shirt_text='Chess'

#finally saving the avtaar
).render("avatar_text.svg")


