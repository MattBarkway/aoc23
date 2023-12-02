mod day_1;
mod utils;
mod day_2;

fn main() {
    match day_1::day_1() {
        Ok(()) => println!("Day 1 completed!"),
        Err(e) => println!("{}", e)
    }
}
