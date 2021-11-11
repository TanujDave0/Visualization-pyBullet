import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -10)

class visualise:
    movable = []
    movId = []
    force = 0
    debug = False

    def __init__(self, humFile, planeFile, force=240, time = 1./240.):
        if humFile[-4::1] == "mjcf":
            self.humId = p.loadMJCF(humFile)
        elif humFile[-3::1] == "xml":
            temp = p.loadMJCF(humFile)
            self.humId = temp[1]
        elif humFile[-4::1] == "urdf":
            self.humId = p.loadURDF(humFile)
        else:
            print("***please provide a urdf or mjcf file for humanoid***")

        if planeFile[-4] == "mjcf":
            self.humId = p.loadMJCF(planeFile)
        elif planeFile[-4] == "urdf":
            self.humId = p.loadURDF(planeFile)
        else:
            print("***please provide a urdf or mjcf file for plane***")

        self.force = force
        self.time = time

        for i in range(p.getNumJoints(self.humId)):
            info = p.getJointInfo(self.humId, i)
            if info[2] == p.JOINT_REVOLUTE:
                self.movable.append(i)

    def debugParam(self):
        self.debug = True
        for i in range(p.getNumJoints(self.humId)):
            info = p.getJointInfo(self.humId, i)
            if info[2] == p.JOINT_REVOLUTE:
                self.movId.append(p.addUserDebugParameter(
                    info[1].decode("utf-8"), -2, 2, 0))
                print(F'Joint: {info[1]}, ID: {i}')

    def step(self):
        self.debug2()
        p.stepSimulation()
        time.sleep(self.time)

    def debug2(self):
        if self.debug:
            for j in range(len(self.movId)):
                tP = p.readUserDebugParameter(self.movId[j])
                self.moveToPos(j, tP)

    def moveToPos(self, id, toPos):
        p.setJointMotorControl2(
            self.humId, self.movable[id], p.POSITION_CONTROL, toPos, force = self.force)

def main():
    trial = visualise("mjcf/humanoid.xml", "plane.urdf", 100)
    trial.debugParam()
    i = 0

    while(1):
        trial.step()
        trial.moveToPos(0, i)
        i += 0.003

main()
