from djitellopy import TelloSwarm
import time

swarm = TelloSwarm.fromFile("swarmUnico.txt")

swarm.connect()
swarm.takeoff()
swarm.move_up(200)
time.sleep(1)
swarm.move_right(120)
time.sleep(1)
swarm.move_right(120)
time.sleep(1)
swarm.move_down(100)
time.sleep(1)
swarm.move_left(120)
time.sleep(1)
swarm.move_left(120)
time.sleep(1)
swarm.land()

