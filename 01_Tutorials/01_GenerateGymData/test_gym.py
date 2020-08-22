import gym
import gym_witches_multiv2

if __name__ == '__main__':
    ## Setup Env:
    env_name      = "Witches_multi-v2"

    # creating environment
    print("Creating model:", env_name)
    env = gym.make(env_name)

    # Setup General Params
    state_dim  = env.observation_space.n
    action_dim = env.action_space.n

    for i in range(steps):
        player =  env.my_game.active_player
        action = policy.act(state, batches[player])# <- state is appended to memory in act function
        state, rewards, done, _ = env.step(action)
