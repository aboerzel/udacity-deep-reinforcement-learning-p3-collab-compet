BUFFER_SIZE = int(5e5)          # replay buffer size
BATCH_SIZE = 128                # minibatch size
GAMMA = 0.99                    # discount factor
TAU = 5e-3                      # for soft update of target parameters
LR_ACTOR = 1e-3                 # learning rate of the actor
LR_CRITIC = 1e-3                # learning rate of the critic
WEIGHT_DECAY = 0                # L2 weight decay
EPISODES = 10000                # max number of episodes
