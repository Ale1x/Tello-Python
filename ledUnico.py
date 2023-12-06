from djitellopy import TelloSwarm
import time

swarm = TelloSwarm.fromFile("ips/swarmUnDrone.txt")

swarm.connect()
swarm.takeoff()

time.sleep(1)
swarm.parallel(lambda i, tello: print(tello.get_battery()))
swarm.move_up(100) #^
time.sleep(1)
swarm.flip("f")
time.sleep(1)
swarm.land()
swarm.end()

