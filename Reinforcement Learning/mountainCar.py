import gym
env = gym.make('MountainCar-v0')

env.reset()

finished = False

while not finished:
	env.step(1)
	env.render()
