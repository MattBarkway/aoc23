mod day_1;
mod day_2;
mod utils;

fn main() {
    match day_1::pt_1() {
        Ok(sum) => println!("Day 1: {}!", sum),
        Err(e) => println!("{}", e),
    }
    match day_1::pt_2() {
        Ok(sum) => println!("Day 1: {}!", sum),
        Err(e) => println!("{}", e)
    }
}
