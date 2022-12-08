use pyo3::prelude::*;
mod npc_player;
mod npc_sensor;
mod enviroment;
mod qbrain;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn qlearning(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    Ok(())
}

#[pymodule]
fn npc_start(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(enviroment::npc_start, m)?)?;
    Ok(())
}

// return x,y,z :usize
// Ok((x,y,z):usize)

/*
できたこと
qbrainの実装

途中
npc_sensorでの世界情報の受け取り
enviromentの設計
保存の仕方

*/