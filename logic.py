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

        print(self.leftWall)
        print(self.midWall)
        print(self.rightWall)

        self.callout = callout

        print(self.callout)


        self.solve()

    def final(self):
        if callout[0] in self.leftWall:
            return False
        elif callout[1] in self.midWall:
            return False
        elif callout[2] in self.rightWall:
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

        if wall != self.leftWall and shape in self.leftWall:
            return leftWall
        elif wall != self.midWall and shape in self.midWall:
            return self.midWall
        elif wall != self.rightWall and shape in self.rightWall:
            return self.rightWall
        
    def swap(self, wallOne, indexOne, wallTwo, indexTwo):
        tempOne = wallOne[indexOne]
        tempTwo = wallTwo[indexTwo]

        wallOne[indexOne] = tempTwo
        wallTwo[indexTwo] = tempOne

    def swapMessage(self, wallOne, shapeOne, wallTwo, shapeTwo):
        if wallOne == self.leftWall:
            if wallTwo == self.midWall:
                message = f'Step {i}: Left dunk {shapeOne} on mid. Mid dunk {shapeTwo} on left.'
            elif wallTwo == self.rightWall:
                message = f'Step {i}: Left dunk {shapeOne} on right. Right dunk {shapeTwo} on left.'

        elif wallOne == self.midWall:
            if wallTwo == self.leftWall:
                message = f'Step {i}: Mid dunk {shapeOne} on left. Left dunk {shapeTwo} on mid.'
            elif wallTwo == self.rightWall:
                message = f'Step {i}: Mid dunk {shapeOne} on right. Right dunk {shapeTwo} on mid.'

        elif wallOne == self.rightWall:
            if wallTwo == self.leftWall:
                message = f'Step {i}: Right dunk {shapeOne} on left. Left dunk {shapeTwo} on right.'
            elif wallTwo == self.midWall:
                message = f'Step {i}: Right dunk {shapeOne} on mid. Mid dunk {shapeTwo} on right.'
        else:
            message = 'Error'
        return message

    def solve(self):


        i = 0
        
        while not self.final():
            # phase one
            # left side swaps
            #print('Initial: ', leftWall)
            while not self.double(self.leftWall):
                swapShapeOne = self.swapShapeFirst(self.leftWall, self.callout[0])
                swapWall = self.checkForShape(self.leftWall, self.callout[0])
                self.swap(self.leftWall,self.leftWall.index(swapShapeOne),swapWall,swapWall.index(self.callout[0]))
                i+=1
                print(self.swapMessage(self.leftWall,swapShapeOne, swapWall,self.callout[0]))
            #print('Final: ', leftWall)

            # mid side swaps
            #print('\nInitial: ', midWall)
            while not self.double(self.midWall):
                swapShapeOne = self.swapShapeFirst(self.midWall, self.callout[1])
                swapWall = self.checkForShape(self.midWall, self.callout[1])
                self.swap(self.midWall,self.midWall.index(swapShapeOne),swapWall,swapWall.index(self.callout[1]))
                i+=1
                print(self.swapMessage(self.midWall,swapShapeOne, swapWall,self.callout[1]))
            #print('Final: ', midWall)

            # right side swaps
            #print('\nInitial: ', rightWall)
            while not self.double(self.rightWall):
                swapShapeOne = self.swapShapeFirst(self.rightWall, self.callout[2])
                swapWall = self.checkForShape(self.rightWall, self.callout[2])
                self.swap(self.rightWall,self.rightWall.index(swapShapeOne),swapWall,swapWall.index(self.callout[2]))
                i+=1
                print(self.swapMessage(self.rightWall,swapShapeOne, swapWall,self.callout[2]))
            #print('Final: ', rightWall)

            # phase two

            i+=1
            print(f'Step {i}: Left dunk {self.leftWall[0]} on mid. Mid dunk {self.midWall[0]} on left.')
            self.swap(self.leftWall,0,self.midWall,0)

            i+=1
            print(f'Step {i}: Mid dunk {self.midWall[1]} on right. Right dunk {self.rightWall[1]} on mid.')
            self.swap(self.midWall,1,self.rightWall,1)

            i+=1
            print(f'Step {i}: Left dunk {self.midWall[1]} on right. Right dunk {self.rightWall[0]} on Left.')
            self.swap(self.leftWall,1,self.rightWall,0)
            



