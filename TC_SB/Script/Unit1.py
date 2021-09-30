def ReadWholeFile():
  file = ProjectSuite.Path + "\parameters.txt"  
  s = aqFile.ReadWholeTextFile(file, aqFile.ctANSI)
  Log.Message("File entire contents:")
  Log.Message(s)
Project.Variables.URL = s