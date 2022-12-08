

pub struct Agent {
    pub reward: f32,
    pub is_done: bool,

}

impl Agent {
    pub fn new() -> Agent {
        Agent {
            reward: 0.0,
            is_done: false,
        }
    }

    pub fn get_state(&self) {
        //センサーから世界の情報を受けとる
        // pythonからボードの情報らをもらう

        //一定の処理をしてstateを返す
    }

    pub fn get_action_from_index(&self,action_idx:usize) -> usize{
        //indexからactionを返す
        0
    }

    pub fn excute_action(&self,action:usize) {
        //actionを実行する
    }

    pub fn set_reward(&self,reward:f32) {
        //rewardをセットする
    }


}