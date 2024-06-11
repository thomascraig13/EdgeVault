leftWall = ['square','circle']
midWall = ['circle','triangle']
rightWall = ['triangle','square']

callout = ['square','circle','triangle']

i = 0

class Solve:

    def __init__(self, shapesOne,shapesTwo,shapesThree,callout):
        self.leftWall = shapesOne
        self.midWall = shapesTwo
        self.rightWall = shapesThree

        self.callout = callout


        self.solve(shapesOne,shapesTwo,shapesThree,callout)

    def final(self):
        if callout[0] in leftWall:
            return False
        elif callout[1] in midWall:
            return False
        elif callout[2] in rightWall:
            return False
        else:
            return True

    def double(self,wall):
        if wall[0] == wall[1]:
            return True
        else:
            return False
        
    def swapShapeFirst(self,wall,callout):
        for shape in wall:
            if callout != shape:
                return shape
                quit

    def swapShapeSecond(self,wall,callout):
        for shape in wall:
            if callout == shape:
                return shape
                quit

    def checkForShape(self, wall, shape):

        if wall != leftWall and shape in leftWall:
            return leftWall
        elif wall != midWall and shape in midWall:
            return midWall
        elif wall != rightWall and shape in rightWall:
            return rightWall
        
    def swap(self, wallOne, indexOne, wallTwo, indexTwo):
        tempOne = wallOne[indexOne]
        tempTwo = wallTwo[indexTwo]

        wallOne[indexOne] = tempTwo
        wallTwo[indexTwo] = tempOne

    def swapMessage(self, wallOne, shapeOne, wallTwo, shapeTwo):
        if wallOne == leftWall:
            if wallTwo == midWall:
                message = f'Step {i}: Left dunk {shapeOne} on mid. Mid dunk {shapeTwo} on left.'
            elif wallTwo == rightWall:
                message = f'Step {i}: Left dunk {shapeOne} on right. Right dunk {shapeTwo} on left.'

        elif wallOne == midWall:
            if wallTwo == leftWall:
                message = f'Step {i}: Mid dunk {shapeOne} on left. Left dunk {shapeTwo} on mid.'
            elif wallTwo == rightWall:
                message = f'Step {i}: Mid dunk {shapeOne} on right. Right dunk {shapeTwo} on mid.'

        elif wallOne == rightWall:
            if wallTwo == leftWall:
                message = f'Step {i}: Right dunk {shapeOne} on left. Left dunk {shapeTwo} on right.'
            elif wallTwo == midWall:
                message = f'Step {i}: Right dunk {shapeOne} on mid. Mid dunk {shapeTwo} on right.'
        return message

    def solve(self,shapesOne,shapesTwo,shapesThree,callout):

        self.leftWall = shapesOne
        self.midWall = shapesTwo
        self.rightWall = shapesThree

        self.callout = callout

        self.i = 0
        
        while not self.final():
            # phase one
            # left side swaps
            #print('Initial: ', leftWall)
            while not self.double(leftWall):
                swapShapeOne = self.swapShapeFirst(leftWall, callout[0])
                swapWall = self.checkForShape(leftWall, callout[0])
                self.swap(leftWall,leftWall.index(swapShapeOne),swapWall,swapWall.index(callout[0]))
                self.i+=1
                print(self.swapMessage(leftWall,swapShapeOne, swapWall,callout[0]))
            #print('Final: ', leftWall)

            # mid side swaps
            #print('\nInitial: ', midWall)
            while not self.double(midWall):
                swapShapeOne = self.swapShapeFirst(midWall, callout[1])
                swapWall = self.checkForShape(midWall, callout[1])
                self.swap(midWall,midWall.index(swapShapeOne),swapWall,swapWall.index(callout[1]))
                self.i+=1
                print(self.swapMessage(midWall,swapShapeOne, swapWall,callout[1]))
            #print('Final: ', midWall)

            # right side swaps
            #print('\nInitial: ', rightWall)
            while not self.double(rightWall):
                swapShapeOne = self.swapShapeFirst(rightWall, callout[2])
                swapWall = self.checkForShape(rightWall, callout[2])
                self.swap(rightWall,rightWall.index(swapShapeOne),swapWall,swapWall.index(callout[2]))
                self.i+=1
                print(self.swapMessage(rightWall,swapShapeOne, swapWall,callout[2]))
            #print('Final: ', rightWall)

            # phase two

            self.i+=1
            print(f'Step {i}: Left dunk {leftWall[0]} on mid. Mid dunk {midWall[0]} on left.')
            self.swap(leftWall,0,midWall,0)

            self.i+=1
            print(f'Step {i}: Mid dunk {midWall[1]} on right. Right dunk {rightWall[1]} on mid.')
            self.swap(midWall,1,rightWall,1)

            self.i+=1
            print(f'Step {i}: Left dunk {midWall[1]} on right. Right dunk {rightWall[0]} on Left.')
            self.swap(leftWall,1,rightWall,0)
            



