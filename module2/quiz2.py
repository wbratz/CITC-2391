def get_volume(width, height, length=2):
    volume = width * height * length
    return volume

def main():
    l = 3
    w = 4
    h = 5
    v = get_volume(l, w, h)
    print(v)
   
if __name__ == "__main__":
    main()