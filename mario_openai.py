import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

# Wrapping simplifies AI learning the movements
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env,SIMPLE_MOVEMENT)

restart = True
for frame in range(1000):
    # A random action
    if restart:
        env.reset()
        restart = False
    state,reward,done,info = env.step(env.action_space.sample())
    # Show the game
    env.render()
env.close()

