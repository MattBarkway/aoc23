use std::io::Error;
use regex::Regex;
use crate::utils::loader::load_input;

pub(crate) fn day_1() -> Result<(), String>{
    let lines = load_input("1.txt").map_err(|e| "Couldn't load soz")?;
    for line in lines {
        let re = Regex::new(r"(\d)").map_err(|e| "".to_owned() )?;
        let mut results = vec![];
        for (_, [number]) in re.captures_iter(&line.map_err(|e| "invalid line lol")?).map(|c| c.extract()) {
            results.push(number::i32);
        }
        // println!("{:?}", results);
    }
    Ok(())
}