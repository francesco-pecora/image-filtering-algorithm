"""
@class:  CSC382
@author: Francesco Pecora
@date:   12/07/2020
"""

import cv2

class ImageFilterMedian:
    def __init__(self, img, windowSize = 1):
        self.img = img
        self.windowSize = windowSize
    
    def filterImage(self):
        rows = len(self.img)
        cols = len(self.img[0])
        for row in range(rows):
            for col in range(cols):
                self.img[row][col] = self.findMedianOfNeighbours(row, col)
        return self.img
    
    def findMedianOfNeighbours(self, row, col):
        neighbours = self.getNeighbours(row, col)
        neighbours.sort()
        return neighbours[len(neighbours) // 2]

    def getNeighbours(self, row, col):
        topLeft = (row - self.windowSize, col - self.windowSize)
        bottomRight = (row + self.windowSize, col + self.windowSize)
        return self.traverseSubWindow(topLeft, bottomRight)

    def traverseSubWindow(self, topLeft, bottomRight):
        neighbours = []
        for row in range(topLeft[0], bottomRight[0] + 1):
            for col in range(topLeft[1], bottomRight[1] + 1):
                if self.isInBounds(row, col):
                    neighbours.append(self.img[row][col])
        return neighbours
    
    def isInBounds(self, row, col):
        rowsInBound = False
        colsInBound = False
        if row > 0 and row < len(self.img) - 1:
            rowsInBound = True
        if col > 0 and col < len(self.img[0]) - 1:
            colsInBound = True
        return rowsInBound and colsInBound
            

                
if __name__ == '__main__':
    # getting the image in gray scale to avoid
    # the three layers of depth due to colors
    img = cv2.imread('./noisy.jpg', cv2.IMREAD_GRAYSCALE)
    windowSize = int(input("Please enter the window size (suggested value between 1-5)"))
    
    # filtering the image
    filter = ImageFilterMedian(img, windowSize)
    newImg = filter.filterImage()
    
    # showing the original image and new filtered image
    cv2.imshow('before', cv2.imread('./noisy.jpg', cv2.IMREAD_GRAYSCALE))
    cv2.imshow('after', newImg)
    
    # wait until windows closed and close i/o with image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
