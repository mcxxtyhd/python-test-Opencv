#将gif图片转成PNG图片
from PIL import Image

im = Image.open('test/test1.gif')
def iter_frames(im):
    try:
        i= 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass
for i, frame in enumerate(iter_frames(im)):
    frame.save('test/test1.jpg',**frame.info)