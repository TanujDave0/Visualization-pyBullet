import sys
sys.path.append("C:\\Program Files (x86)\\Vicon\\Nexus2.9\\SDK\\Win32")
sys.path.append('C:\\Program Files (x86)\\Vicon\\Nexus2.9\\SDK\\Python')
import ViconNexus
import time

from udp import udpServer

# from vicon_dssdk import ViconDataStream
 
# client = ViconDataStream.Client()
# print(client.Connect('localhost:801'))
# client.GetFrameNumber()


vicon = ViconNexus.ViconNexus()

class demo:
    def __init__(self):
        self.subjects = vicon.GetSubjectNames()
        self.server = udpServer()
    
    def getMarkers(self, i):
        self.markers = vicon.GetMarkerNames(self.subjects[i-1])
    
    def printAllSubjects(self):
        print("Printing subject names")
        for i in range(len(self.subjects)):
            print(" ", i+1, ": ", self.subjects[i])
    
    def printMarkerNames(self):
        for j in range(len(self.markers)):
            print(" Marker", j+1, self.markers[j].encode('utf-8'))
    
    def printCoordinates(self, i):
        for f in self.markers:
            print("   Marker: ", f.encode('utf-8'))
            traj = vicon.GetTrajectory(self.subjects[i-1], f)
            print("    Last x coordinate: ", traj[0][len(traj[0])-1])
            print( "    Last x coordinate: ", traj[1][len(traj[0])-1])
            print("    Last x coordinate: ", traj[2][len(traj[0])-1])
    
    def startTime(self):
        self.start_time = time.time()
    
    def printTime(self):
        print ("Time taken : %s seconds" %(time.time()-self.start_time))
    
    def sendData(self, data):
        self.server.send(data)


# trial = demo()
# trial.startTime()
# trial.printAllSubjects()
# trial.getMarkers(1)
# trial.printCoordinates(1)
# trial.printTime()
