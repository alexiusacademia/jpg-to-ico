A small script that converts a given jpg file to ico file. Useful when you need an icon file with multiple sizes.

## Usage

1. Clone this repository `git clone https://github.com/alexiusacademia/jpg-to-ico.git`
2. Create a virtual environment.
3. Activate the virtual environment
4. Install the requirements `pip install -r requirements.txt`
5. Copy a path to an input file. For example `input.jpg` if you place it inside this code's folder
6. Decide where you want to put the out. If inside the same directory as this program, just set it to `output.ico` (You can change output to any name you want or need)
7. Edit the `main.py`
```py
if __name__ == '__main__':
    jpg_to_ico('input.jpg', 'output.jpg')
```
9. Save and run the script.

```bash
python main.py
```
