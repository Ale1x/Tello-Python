from djitellopy import TelloSwarm
import time

swarm = TelloSwarm.fromFile("ips/swarmUno.txt")

swarm.connect()
swarm.takeoff()

time.sleep(1)
swarm.parallel(lambda i, tello: print(tello.get_battery()))
swarm.move_up(100) #^
time.sleep(1)
swarm.move_right(50) #>
time.sleep(1)
#tello.move_right(120) #>
time.sleep(1)
swarm.parallel(lambda i, tello: tello.move_up(50 + i * 10) if i in [0, 1] else tello.move_down(50 + (i-2) * 10))
time.sleep(1)
swarm.move_forward(30) 
time.sleep(1)
swarm.move_back(30)
time.sleep(1)
swarm.parallel(lambda i, tello: print(tello.get_battery()))
swarm.parallel(lambda i, tello: tello.move_down(50 + i * 10) if i in [0, 1, 2] else tello.move_up(50 + (i-2) * 10))
time.sleep(1)
swarm.move_left(50)
time.sleep(1)
swarm.parallel(lambda i, tello: print(tello.get_battery()))
swarm.parallel(lambda i, tello: tello.move_up(50 + i * 10) if i in [0, 1, 2] else tello.move_down(50 + (i-2) * 10))
time.sleep(1)
swarm.move_forward(100)
time.sleep(1)
swarm.move_back(100)
time.sleep(1)
swarm.parallel(lambda i, tello: print(tello.get_battery()))
swarm.parallel(lambda i, tello: tello.move_down(50 + i * 10) if i in [0, 1, 2] else tello.move_up(50 + (i-2) * 10))
time.sleep(1)
swarm.move_right(50)
tello.flip("b")
time.sleep(1)
swarm.flip("f")
time.sleep(4)
swarm.parallel(lambda i, tello: print(tello.get_battery()))
swarm.land()
swarm.end()

