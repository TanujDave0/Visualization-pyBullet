import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-10)

#---------loadBotlab-------------
# objs = p.loadSDF("resources/botlab/botlab.sdf", globalScaling=2.0)
# zero=[0,0,0]
# p.configureDebugVisualizer(p.COV_ENABLE_RENDERING,1)
# print("converting y to z axis")
# for o in objs:
#     pos,orn = p.getBasePositionAndOrientation(o)
#     y2x = p.getQuaternionFromEuler([3.14/2.,0,3.14/2])
#     newpos,neworn = p.multiplyTransforms(zero,y2x,pos,orn)
#     p.resetBasePositionAndOrientation(o,newpos,neworn)

#----------loadHum2----------
obUids = p.loadMJCF("mjcf/humanoid.xml")
humId = obUids[1]

#--------debugParam----------
# movable = []
# movId = []
# for i in range(p.getNumJoints(humId)):
#     info = p.getJointInfo(humId, i)
#     if info[2] == p.JOINT_REVOLUTE:
#         movable.append(i)
#         movId.append(p.addUserDebugParameter(info[1].decode("utf-8"), -2, 2, 0))
#         print(F'Joint: {info[1]}, ID: {i}')

# p.setPhysicsEngineParameter(numSolverIterations=10)
# p.changeDynamics(humId, -1, linearDamping=0, angularDamping=0)

while(1):
    p.stepSimulation()
    time.sleep(1./240.)

    # f = 10
    # for j in range(len(movId)):
    #     tP = p.readUserDebugParameter(movId[j])
    #     p.setJointMotorControl2(humId, movable[j], p.POSITION_CONTROL, tP, force=5 * 240.)

p.disconnect()