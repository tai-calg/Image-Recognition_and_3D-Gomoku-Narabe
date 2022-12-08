use crate::{qbrain::QBrain, npc_sensor::Agent};

pub struct QEnv {
    qbrain: QBrain,
    prev_state : usize,
    learning_agent : Agent,
    

}

pub fn npc_start() -> QEnv {
    let qbrain = QBrain::new();
    let agent = Agent::new();
    let prev_state = agent.get_state(); //todo

    let env = QEnv {
        qbrain : qbrain,
        prev_state: prev_state,
        learning_agent: agent,
    };

    return env;

}

impl QEnv {

    pub fn loop_update(&self) {
        loop {
            self.agent_update(self.learning_agent, self.qbrain);

            //write qtable to a file 
            //self.qbrain.save_qtable();

        }
    }

    pub fn agent_update(&self, ag:Agent, mut b:QBrain) {
        let aciton_index = b.get_action(self.prev_state as i32);

        let action = ag.get_action_from_index(aciton_index);

        ag.excute_action(action);

        let new_state = ag.get_state();
        b.update_qtable(self.prev_state,new_state, aciton_index, ag.reward, ag.is_done);
        ag.set_reward(0.0);
        self.prev_state = new_state;

    }
}