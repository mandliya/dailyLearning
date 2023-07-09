- # Unit 1
    - ## What is Reinforcement Learning?
        - An AI agent learns from environment by interacting with it through trial and error.
        - It receives rewards for taking actions (Positive or Negative) and use those rewards to take next action.
        - The overall goal of the agent is to maximize the cumulative rewards it receives.
        - Reinforcement learning is just a computational approach of learning from actions. Just how humans and animals learn.
        - Formally, RL is a framework for solving control tasks also called decision problems by building agents which learn from environment by interacting it with through trial and error and receiving rewards (positive or negative) as unique feedback.
    - ## RL process:
        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FDr6BYBKcZH.png?alt=media&token=0f578c9f-29f9-43b9-b18b-4255ab37f229)
        - A loop of state, action, reward and next state.
        - Imaging an agent learning to play a game.
            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FQ155aY3ELI.png?alt=media&token=337f98de-377a-47cb-80ac-44396b704f26)
            - Agent starts a $S_0$ state received from the __Environment__ - We receive the first frame of the game.
            - Based on state $S_0$, the agent takes action $A_0$. - Our agent moves to right.
            - The environment goes to new state $S_1$ - new frame.
            - The environment gives some reward $R_1$ to the agent - We are not dead yet (Positive reward +1).
            - The loop continuous for the next states $S_2, S_3 ... S_n$
            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FkQWARFLbxt.png?alt=media&token=aeee252a-8cdf-453e-ac81-bebd10c5960e)
            - The goal of the agent is to **maximize the cumulative reward** it receives. It is also called **the expected return**.
    - ## The reward hypothesis: The central idea of RL
        - Why is the goal of the agent is to maximize the expected return?
            - Because RL is based on __reward hypothesis__ that any goal can be described as the **maximization of the expected return** (expected cumulative reward).
            - Hence in RL, to have the best behavior, we aim to learn to take actions that maximizes the overall expected cumulative reward.
    - ## Markov Property
        - RL process is often described as **Markov Decision Process**.
        - The Markov Property implies that our agent **only needs current state** to decide what action to take and **not the history of all states and actions.**
        - 
    - ## Observations/States Space
        - Observations or states are the **information our agent receives from the environment.**. In case of a video game, it could be a frame or screenshot. In case of trading, it could be current value of a stock.
        - ### Difference between observations and states 
            - There is indeed a difference between observation and state. 
            - **State** __s__: The state denotes a **complete description of the state of the world in which agent is operating**. There is __no hidden information__.  E.g. In a game of chess, the agent usually have information of all the 64 squares.
                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FUQnUKoTL7n.png?alt=media&token=3d5c2e24-4e37-48fc-8f34-09a78289dcdd)
            - **Observation** __o__: Observation often refers to partial description of the state. The agent doesn't have complete information of the whole environment, instead it only receives the relevant information to take actions.
                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FCZmrQtMNXl.png?alt=media&token=7745d780-4c81-40f5-b4b7-a3d832215488)
                - In Super Mario Bros, we only see the part of the level close to the player, so we receive an __observation__. We are in a __partially observed environment__. We receive an observation since we only see a part of the level.
            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2F9adDJ4ygIG.png?alt=media&token=cc4db638-dd2f-4b51-b82c-3108f6c67fab)
            - 
    - ## Action Space
        - The action space is the **set of all possible actions in an environment**.
        - The action space can be __discrete__ or __continuous__ space.
            - __Discrete Space__: The number of possible actions is finite. In a game of Super Mario Bros, the only actions an agent can takes are move in 4 directions and say jump.
                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FJAXQXkeMj8.png?alt=media&token=c44a9913-1e7a-4be9-ab53-c45c6f74c255)
            - __Continuous Space__: The number of possible actions an agent can take is infinite. A self driving agent may take actions from an infinite space. E.g. turn 20', 40', 20.2', apply brakes, honk, increase speed by 5 miles, decrease speed by 2.2 miles.
                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FCQkUnP1sZm.png?alt=media&token=07dc3958-6625-40b1-995f-f5c777b89d0a)
            - 
        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2F47ZexWxZ5f.png?alt=media&token=a1c8904f-08d1-4efc-a8fe-11f44252b82b)
    - ## Rewards and the discounting
        - The rewards are the most important component of the process. It is the only feedback an agent receives. It tells agent if an action taken was good or bad.
        - The cumulative reward at each time step **t** can be written as
            - $R(\tau) = r_{t+1} + r_{t+2} + r_{t+3}...$
            - The cumulative reward equals sum of all rewards in the sequence.
            - Which is equivalent to:
                - $R(\tau) = \sum_{k=0}^{\infty}r_{t+k+1}$
        - However, if we just add them like this, we are assigning equal weight to each award we receive in future.
        - The reward which comes sooner (say at the beginning of the game) is more likely to happen than future rewards, as they are more predictable.
        - Consider our agent the mouse in this game:
            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FDm1Frs4QWJ.png?alt=media&token=20ac9363-c58c-4d0a-bfe2-9f60c9218d23)
            - The mouse can move one tile each time step, and the opponent is the cat, which can move too.
            - The mouse's goal is to eat maximum amount of cheese before being eaten by the cat.
            - From the diagram, we can see it is more probable for mouse to eat cheese near it, rather than the cheese close to cat. (The closer mouse is to the cat, more dangerous it is.)
            - Thus, the reward near the cat, even if it is bigger (e.g. more cheese) will be discounted, as we are less sure that we'll be able to reach there.
        - This is how the reward discounting works.
            - We define a discount factor $\gamma$ which is between 0 and 1.
            - Most of the times it's value is between 0.95 to 0.99.
            - The **larger the gamma** the smaller the discount. This means our agent cares **more about long-term reward**.
            - The **smaller the gamma**, the bigger the discount. This means our agent cares more about the **short term rewards**. (The nearest cheese)
            - Each future reward is discounted by gamma raised to the power of time step. In other words the farther the reward is in the future, lesser it's contribution to the cumulative reward.
                - $R(\tau) = r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3}... $
                - $R(\tau) = \sum_{k=0}^{\infty}\gamma^k r_{t+k+1}$
                - 
            - 
    - ## Types of tasks
        - task is an **instance** of a Reinforcement Learning problem. Let's explain it with a maze problem.
        - Imagine an agent navigating a maze. Each time "step" would involve the agent taking an action - moving in one of the directions north, south, east or west. The environment rewards this action either positively (moving closer to exit) or negatively (hitting a wall), and finally agent transitions to a new state*. The task or an episode is the full sequence of these steps from when the agent first enters the maze to when it reaches the exit. (the termination condition).
            - *Note that here, agent is not really changing, it means that agent's perception of the environment is changing. The state is representation of the environment from the perspective of the the agent. When agent takes an action, it influences the environment and results in a new representation or a new state. 
        - Another example of task is when an agent plays a game of chess and it ends either in draw, win or defeat. The task would being with the initial game board setup and would continue through each move (which involve the agent observing the state of the board, deciding on an action/move, and receiving a reward or penalty) until the game concludes. The conclusion (or terminal state) of the game would be a win, loss, or draw.
        - Note that not all tasks have terminal state and they might continue forever.
        - There are two types of tasks.
            - **Episodic tasks**: In episodic tasks, we have a starting point, and an ending point (a terminal state). This creates an episode which contains:
                - A list of States, Actions, Rewards and next States.
                - The chess example above is an example of episodic task. Another example is a level in video game. It concludes by player is killed or we have reached end of the level.
            - **Continuous tasks**: These are the tasks that continue forever (no terminal state). In this case, the agent must learn to how to choose the best actions and simultaneously interact with the environment.
                - Cartpole problem
                - An agent that does automated stock trading. For this, there is no starting point or terminal state. The agent keeps running until we decide to stop it.
            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2Ft5HxWmIXla.png?alt=media&token=8ad7b928-be52-466b-979b-dd6452b72502)
            - 
    - ## The Exploration/Exploitation Trade off
        - __Exploration__ is when an agent explores the environment by taking random actions to learn more about the environment.
        - __Exploitation__ is when an agent exploits the knowledge it has already acquired to maximize the reward.
        - We need to balance the exploration and exploitation. 
        - Go back to agent mouse:
            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FApMAkOoYjo.png?alt=media&token=9aca040a-ff4a-4ea0-a9d6-3f6d3112aeb7)
            - The diagram might be a bit confusing, the rewards on the cheese is +1 but infinite amount of times.
            - Our mouse can have an infinite amount of small cheese (+1), but at the top of the maze there is gigantic sum of cheese (+1000).
            - If we only focus on exploitation, our agent will never reach the large sum of cheese, instead it will only exploit the nearest source of rewards, even if this source is small.
            - If our agent does a little bit of exploration, it can discover the big reward.
            - We need to balance how much we explore the environment, and how much we exploit what we know about the environment.
        - Restaurant problem:
            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FHBc_Xsm-r6.png?alt=media&token=bee31329-04d6-42e0-8b1d-9f86d11cb18b)
            - **Exploitation**: You can either choose to same usual restaurant you have been going to. The risk here is you might be missing on another better restaurant.
            - **Exploration**: Try restaurants you have not tried before, with risk of having a bad experience, but the probable chance of discovering a better food experience.
        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FdJ__pTbGGp.png?alt=media&token=25a3ba41-574f-4e01-afe6-ef57f7ef8fc4)
    - ## Two main approaches for solving RL problems
        - ### The Policy $\pi$: the agent 's brain
            - The Policy $\pi$ is the **brain** of our agent. It is the function that tell us what actions to take given the state we are in. So it **defines the agent's behavior** at a given time.
            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2Fmrilh74Dx3.png?alt=media&token=f5d957f8-cfc3-4c5a-81d0-d4ee890cc425)
            - This mapping or function between state and actions is something the agent learns. 
            - Our goal is to find the __optimal policy__ ($\pi^*$) which maximizes the expected return when the agent acts according to it.
            - There are two approaches to train our agent to find this optimal policy $\pi^*$
                - Approach 1: **Directly**, __by teaching agent to learn which actions to take__, given the current state. These are **Policy-Based Methods** .
                - Approach 2: **Indirectly**, __by teaching the agent to learn which state is more valuable__ and then __take the action that leads to more valuable states__ : **Value-Based Methods**
                - 
        - ### Policy-Based Methods
            - We learn the policy function directly.
            - This function will define the mapping of each state to the best corresponding action. Alternatively, it could be a **probability distribution over the set of possible actions at that state.**.
            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FhG-E1R-hmZ.png?alt=media&token=d024d85b-6ee0-4e9b-b476-c34ecbb0905d)
                -  the policy (deterministic) directly indicates the action to take for each step.
            - We will have two types of policies:
                - __Deterministic__: a policy at a given state will always return the same action.
                    - $a = \pi(s)$
                - __Stochastic__: outputs a probability distribution over actions
                    - $\pi(a | s) = P[A|s]$
                    - policy(actions | state) = probability distribution over the set of actions given the current state
                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FLMNA5nAcv1.png?alt=media&token=2f1b084a-1951-430d-a9b4-cb4be257d0bd)
                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FAJ3AWPzxqJ.png?alt=media&token=dacdd14b-24cd-4696-9709-ae99e4651cd7)
                - 
        - ### Value-Based Methods
            - This is the indirect method, where instead of directly learning policy, we learn a **value function** that __maps a state to the expected value of being at that state__.
            - The value of a state is the __expected discounted return__ that agent can get if it __starts in that state and then acts according to our policy__.
                - **acts according to our policy** : Just means that our policy is going to the next state with highest value
            - $V_\pi(s) = \mathbb{E}[R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3}....| S_t = s]$
            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FshPXHMg1b8.png?alt=media&token=5e212437-2197-441a-9f53-6d2a154530f4)
                - Thanks to our value function, at each step our policy will select the state with the biggest value defined by the value function: -7, then -6, then -5 (and so on) to attain the goal.
            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2FJ8gGtPgHBY.png?alt=media&token=addc656d-3d62-4e83-8a9a-8e8cb52dee13)
            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2F-rHJZgm59K.png?alt=media&token=a6c4be08-7e41-4f9f-b57c-3fdcddb60ca8)
        - 
    - ## The “Deep” in Reinforcement Learning
        - We use deep neural networks to solve **RL** problems. Hence the name deep.
        - For example: __Q-learning__ is a classing Value-Based algorithm, where we use traditional algorithm to create a Q table that helps us find what actions to take for each state. On the other hand in __Deep Q-Learning__ we use neural networks to approximate these Q value.
        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdailygrind%2Fg9raqVLM8u.png?alt=media&token=f15c0010-81d3-4f88-ba8f-a5cd53b8393f)
        - 
    - 