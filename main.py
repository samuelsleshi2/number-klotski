from broadcast import stream
import cv2 as cv

def main():
    cap = cv.VideoCapture(1)
    stream(cap)

if __name__ == "__main__":
    main()