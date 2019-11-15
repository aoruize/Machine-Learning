import gym
env = gym.make('MountainCar-v0')

env.reset()

for i in range(1000):
	stepValue = 2
	env.step(stepValue)
	env.render()
