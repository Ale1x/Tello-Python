from djitellopy import TelloSwarm

swarm = TelloSwarm.fromFile("ips/swarmUnDrone.txt")

swarm.connect()
swarm.parallel(lambda i, tello: print(tello.get_battery()))
swarm.end()