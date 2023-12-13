from djitellopy import TelloSwarm
import time

swarm = TelloSwarm.fromFile("ips/swarmUnico.txt")

swarm.connect()
swarm.takeoff()

time.sleep(1)
#swarm.parallel(lambda i, tello: print(tello.get_battery()))
swarm.move_up(100) #^f
time.sleep(3)

swarm.parallel(lambda i, tello: 
    tello.move_up(50) if i in [0, 4] else
    tello.move_up(100) if i in [1, 3] else
    tello.move_up(150) if i in [2, 5] else
    None
)

time.sleep(3)

swarm.parallel(lambda i, tello: 
    tello.move_up(100) if i in [0, 4] else
    tello.move_down(100) if i in [2, 5] else
    None
)

time.sleep(3)

swarm.parallel(lambda i, tello: 
    tello.move_down(50) if i in [0, 4] else
    tello.move_up(100) if i in [1, 3] else
    tello.move_up(50) if i in [2, 5] else
    None
)

time.sleep(3)
swarm.parallel(lambda i, tello: 
    tello.move_up(100) if i in [0, 4] else
    tello.move_up(100) if i in [2, 5] else
    None
)
time.sleep(3)
swarm.parallel(lambda i, tello: 
    tello.move_back(150) if i in [3, 4, 5] else
    None
)
time.sleep(3)
swarm.parallel(lambda i, tello: tello.move_up(50) if i in [0, 1, 2] else tello.move_down(50))
swarm.move_right(120) #>
time.sleep(1)
swarm.move_right(120) #>
time.sleep(1)
swarm.parallel(lambda i, tello: tello.move_up(50) if i in [0, 1, 2] else tello.move_down(50))
time.sleep(1)
swarm.parallel(lambda i, tello: print(tello.get_battery()))
swarm.parallel(lambda i, tello: tello.move_down(50) if i in [0, 1, 2] else tello.move_up(50))
time.sleep(1)
swarm.move_left(120)
time.sleep(1)
swarm.move_left(120)
time.sleep(1)
#swarm.parallel(lambda i, tello: print(tello.get_battery()))
swarm.parallel(lambda i, tello: tello.move_up(50) if i in [0, 1, 2] else tello.move_down(50))
time.sleep(1)
swarm.move_forward(100)
time.sleep(1)
swarm.move_back(100)
time.sleep(1)
swarm.move_left(200)
time.sleep(1)
#swarm.parallel(lambda i, tello: print(tello.get_battery()))
swarm.parallel(lambda i, tello: tello.move_down(50) if i in [0, 1, 2] else tello.move_up(50))
time.sleep(1)
swarm.move_right(200)
time.sleep(1)
swarm.flip("b")
time.sleep(1)
swarm.flip("f")
time.sleep(1)
swarm.parallel(lambda i, tello: tello.move_up(50) if i in [0, 1, 2] else tello.move_down(50))
time.sleep(4)
#swarm.parallel(lambda i, tello: print(tello.get_battery()))
swarm.land()
swarm.end()

