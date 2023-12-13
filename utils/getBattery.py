from djitellopy import TelloSwarm

swarm = TelloSwarm.fromFile("ips/swarmUnico.txt")

swarm.connect()
swarm.parallel(lambda i, tello: print(tello.get_battery()))
swarm.end()