#David Fry
#4-1-13
import os

class Folder(object):
    
    def __init__(self, parentDir, listOfSubDirs):
        ''' Inits the class and the variables use'''
        self.parentDir = parentDir
        self.listOfSubDirs = listOfSubDirs
        
    def makeParent(self):
        ''' Creates a parent directory/folder in the user specfied location
            it also checks to makes sure the directory/folder does not already
            exist. If it does it returns a 1 if not it creates the directory/folder
            
            EXP: my_folder = Folder("/name", "b")
            '''
        
        if type(self.parentDir) == str:
            if os.path.exists(self.parentDir):
                return 1
            else:
                return os.mkdir(self.parentDir)
            
    def sliceSubDirNames(self,*args):
        ''' Takes in a list of sub-directory names as one string. Each sub-directory
            name is sperated by a comma and then seprates each section from a 
            start point to an end point. It useses the comma as a break point.
            
            EXP: String: "name1,name2,name3" = List: ["name1", "name2", "name3"]
              

          '''
        subFolderList = []
        word = ""
        startSlice = 0
        endSlice = 0
        # CASE 1 Default, takes in the value from the constructor listOfSubDirs (needs to be a string)
        if len(args) == 1 and type(args[0]) == str:   
            stringLength = len(self.listOfSubDirs)
            for letter in range(stringLength):
                if self.listOfSubDirs[letter] == ",":
                    endSlice = letter
                    word = self.listOfSubDirs[startSlice:endSlice]
                    subFolderList.append(word)
                    startSlice = endSlice + 1
    
                elif letter == stringLength - 1:
                    endSlice = letter + 1
                    word = self.listOfSubDirs[startSlice:endSlice]
                    subFolderList.append(word)
       
        # CASE 2 User Defined input has to be a string for the folder names
        if len(args) == 2 and type(args[1]) == str:    
            stringLength = len(args[1])
            for letter in range(stringLength):
                if args[1][letter] == ",":
                    endSlice = letter
                    word = args[1][startSlice:endSlice]
                    subFolderList.append(word)
                    startSlice = endSlice + 1
    
                elif letter == stringLength - 1:
                    endSlice = letter + 1
                    word = args[1][startSlice:endSlice]
                    subFolderList.append(word)  
        
        return subFolderList
        
    def makeSubDirs(self, *args):
        '''Takes a list of names with out the commas and makes folders out of the names. The folders are created
           under the given parent directory. It also has the ablity to make more sub folders from a given folder name
           the method takens in a list for one arg. For 2 args it needs a string and a list of names separted by a comma
           
           EXP: makeSubDirs(classObject.listOfSubDirs) or makeSubDirs("", "name", "name1,name2,name3)  
           '''
        # CASE 1: makes the defult values base on the class constructor
        if len(args) == 1 and type(args[0]) == str:
            numOfSubDirs = len(self.sliceSubDirNames(self.listOfSubDirs))
            for folderNum in range(numOfSubDirs):
                os.makedirs(self.parentDir + "/" + self.sliceSubDirNames(self.listOfSubDirs)[folderNum])
        
        # CASE 2: makes sub directories from the given folder and then adds the list of names for the folders
        if len(args) == 3 and type(args[1]) == str and type(args[2]) == str :
            numOfSubDirs = len(self.sliceSubDirNames("", args[2]))
            for folderNum in range(numOfSubDirs):
                os.makedirs(self.parentDir + "/" + args[1] + "/" + self.sliceSubDirNames("", args[2])[folderNum])
    
            



    
