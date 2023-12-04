use crate::utils::loader::load_input;
use crate::utils::types::SimpleResult;

mod day_1;
mod day_2;
mod day_4;
mod utils;

fn main() -> SimpleResult<()> {
    let sum = day_1::pt_1(&load_input("1.txt")?)?;
    println!("Day 1 (pt1): {}!", sum);

    // let answer = day_2::pt_1(&load_input("2.txt")?)?;

    Ok(())
}
