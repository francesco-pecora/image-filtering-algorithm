"""
@class:  CSC382
@author: Francesco Pecora
@date:   12/13/2020
"""

import cv2
from medianDeterministic import DeterministicMedian

class ImageFilterMedian:
    def __init__(self, img, windowSize = 1):
        self.img = img
        self.windowSize = windowSize
        self.median = DeterministicMedian()
    
    def filterImage(self):
        '''
        main function where the filtering of the image starts
        '''
        rows = len(self.img)
        cols = len(self.img[0])
        for row in range(rows):
            for col in range(cols):
                self.img[row][col] = self.findMedianOfNeighbours(row, col)
        return self.img
    
    def findMedianOfNeighbours(self, row, col):
        '''
        function that calls the class finding the median of the window section (neighbours)
        int row: vertical position of the cell to be processed
        int col: horizontal position of the cell to be processed
        '''
        neighbours = self.getNeighbours(row, col)
        neighbours = list(set(neighbours)) # the order statistics algorithm assumes there are no repeating values
        return self.median.kthSmallest(neighbours, 0, len(neighbours) - 1, len(neighbours)//2)

    def getNeighbours(self, row, col):
        '''
        function that identifies the subwindow around the specific cell of the matrix
        int row: vertical position of the cell to be processed
        int col: horizontal position of the cell to be processed
        '''
        topLeft = (row - self.windowSize, col - self.windowSize)
        bottomRight = (row + self.windowSize, col + self.windowSize)
        return self.traverseSubWindow(topLeft, bottomRight)

    def traverseSubWindow(self, topLeft, bottomRight):
        '''
        function that flattens the subWindow into a 1-D array
        int topLeft: integer holding the top left point(x, y) of the subWindow
        int bottomRight: integer holding the bottom left point(x, y) of the subWindow
        '''
        neighbours = []
        for row in range(topLeft[0], bottomRight[0] + 1):
            for col in range(topLeft[1], bottomRight[1] + 1):
                if self.isInBounds(row, col):
                    neighbours.append(self.img[row][col])
        return neighbours
    
    def isInBounds(self, row, col):
        '''
        function that returns whether or not the input values are in bound in the image matrix
        int row: vertical position of the cell to be processed
        int col: horizontal position of the cell to be processed
        '''
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
