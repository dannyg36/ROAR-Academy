import gym
import numpy as np

# Number of episodes to run
EPISODES = 100

class CustomController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def compute_action(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        control_signal = (self.Kp * error) + (self.Ki * self.integral) + (self.Kd * derivative)
        self.prev_error = error
        # Action is 1 if control signal is positive, otherwise 0
        return 1 if control_signal > 0 else 0

# Define the custom controller with chosen parameters
controller = CustomController(Kp=1.0, Ki=0.0, Kd=0.7)

if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    done = False

    for e in range(EPISODES):
        state = env.reset()
        total_reward = 0
        for time in range(500):
            # Extract the pole angle from the state
            pole_angle = state[2]
            # Compute the time step (assuming 50 updates per second)
            dt = 1.0 / 50.0
            # Compute the action using the custom controller
            action = controller.compute_action(pole_angle, dt)
            next_state, reward, done, _ = env.step(action)
            env.render()
            total_reward += reward
            state = next_state
            if done:
                print(f"Episode: {e}/{EPISODES}, Score: {time}, Total Reward: {total_reward}")
                break