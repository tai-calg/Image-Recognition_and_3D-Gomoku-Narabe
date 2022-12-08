//use rand
use rand;

pub struct QBrain {
    pub statesize : usize,
    pub actionsize : usize,
    pub qtable: Vec<Vec<f32>>,
    epsilon : f32,
    epsilon_min : f32,
    annual_steps : i32,
    gamma : f32,
    alpha : f32,
}

impl QBrain{
    pub fn new() -> QBrain{
        QBrain{
            statesize : 64,
            actionsize : 64,
            qtable: vec![vec![0.; 64]; 64],
            epsilon : 1.0,
            epsilon_min : 0.01,
            annual_steps : 1000,
            gamma : 0.95,
            alpha : 0.01,
        }
    }

    pub fn create_table(&mut self) {
        self.qtable = vec![vec![0.0; 64]; 64]; // 64 is state size ,and 64 is action size
    }

    pub fn get_action(&mut self, state :i32) -> usize{
        let mut action = 0;
        // random [0,1]
        if self.epsilon <= rand::random::<f32>() {
            // select argmax qtable[state] commpare f32
            action = self.qtable[state as usize].clone().into_iter().enumerate().max_by(|a, b| a.1.partial_cmp(&b.1).unwrap()).unwrap().0;
            assert_eq!([2.0,1.0, 3.3].into_iter().enumerate().max_by(|a, b| a.1.partial_cmp(&b.1).unwrap()).unwrap().0 , 2);
        } else {
            //random [0,64] by i32
            action = (rand::random::<i32>() % 64) as usize;
        }

        if self.epsilon > self.epsilon_min {
            self.epsilon -= ((1.0 - self.epsilon_min) / self.annual_steps as f32);
        }


        return action as usize;
    }
    pub fn update_qtable(&mut self, laststate :usize, next_state :usize, action :usize, reward :f32, is_done:bool) {

        if next_state != laststate {
            self.qtable[laststate][action] += 
                self.alpha * (reward + self.gamma * self.qtable[next_state].clone().into_iter().reduce(f32::max).unwrap() 
                    - self.qtable[laststate][action]) as f32;
        }else {
            self.qtable[laststate][action] += 
                self.alpha * (reward - self.qtable[laststate][action]) as f32;
        }
    }



}

