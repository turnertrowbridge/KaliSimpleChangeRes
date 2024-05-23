import subprocess
import sys

resolutions = [
    '1024x768',
    '1280x1024',
    '1680x1050',
    '1920x1080',
    '1920x1200'
]

if len(sys.argv) > 1:
    res = sys.argv[1]

else:
    print("Select a resolution:")
    for i, value in enumerate(resolutions, start=1):
        print(f"{i}. {value}")

    choice = input("Enter number (or 'q' to quit): ")

    if choice.lower() == 'q':
        sys.exit()

    res = resolutions[int(choice) - 1]

    if res is None:
        print("Invalid")
        sys.exit()

subprocess.run(f"xrandr --output Virtual-1 --mode {res}", shell=True)
