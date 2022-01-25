from PIL import Image

def get_pillow_img(name):
    pineapple = Image.open(name)
    return pineapple


def img2greyscale(img):
    return img.convert('L')
    #img.save(name[:-4] + '_greyscale.png')

pineapple = get_pillow_img('pineapple.jpg')
gray_pineapple = img2greyscale(pineapple)
#gray_pineapple.show()

color_data = list(pineapple.getdata())
greyscale_data = list(gray_pineapple.getdata())

brainfuck = {
    0:'>',
    1: '<',
    2: '+',
    3: '-',
    4: '.',
    5: ',',
    6: '[',
    7: ']'
}

brainfucked_data = [brainfuck[val % 8] for val in greyscale_data]


def html_from_brainfucked_data(data, size):
    w = size[0]
    h = size[1]
    string = ''
    start, end = 0, w
    for row in range(h):
        string = string + "<br>"
        string += ''.join([str(item) for item in data[start:end]])
        start += w
        end += w

    return string

if __name__ == '__main__':
    html_string = html_from_brainfucked_data(brainfucked_data, gray_pineapple.size)

    with open('test.html','w') as f:
        f.write(html_string)
        f.close()
