use crate::utils::loader::load_input;
use crate::utils::types::SimpleResult;
use clap::Parser;

mod day_1;
mod day_2;
mod utils;

#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
pub struct Args {
    pub day: i32,
}

fn main() -> SimpleResult<()> {
    let args = Args::parse();

    match args.day {
        1 => {
            let sum = day_1::pt_1(&load_input("1.txt")?)?;
            println!("Day 1 (pt1): {}!", sum);
        }
        2 => {
            let input = load_input("2.txt")?;
            let one = day_2::pt_1(&input)?;
            println!("Day 2 (pt1): {}!", one);
            let two = day_2::pt_2(&input)?;
            println!("Day 2 (pt2): {}!", two);
        }
        _ => println!("I've not done that day yet!"),
    }

    // let answer = day_2::pt_1(&load_input("2.txt")?)?;

    Ok(())
}
