from PIL import Image

def jpg_to_ico(jpg_path, ico_path, sizes=[(32, 32), (64, 64), (128, 128), (256, 256)]):
    """
    Converts a jpg file to a set of ico files.

    :param jpg_path: Path to the input jpg file
    :param ico_path: Path to the output
    :param sizes: List of sizes for the icon files.
    """
    img = Image.open(jpg_path)
    img.save(ico_path, format='ICO', sizes=sizes)
    print(f'Converted {jpg_path} to {ico_path}.')


if __name__ == '__main__':
    jpg_to_ico('favicon.jpg', 'favicon.ico')
