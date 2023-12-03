use std::io::Error;
use regex::Regex;
use crate::utils::loader::load_input;

pub(crate) fn day_1() -> Result<(), String> {
    let lines = load_input("1.txt").map_err(|e| "Couldn't load soz")?;
    let mut sum = 0;
    for line in lines {
        sum += get_coords(&line.map_err(|e| "Nope")?)?;
    }
    println!("{}", sum);
    Ok(())
}


fn get_coords(line: &str) -> Result<i32, String> {
    let re = Regex::new(r"(\d)").map_err(|e| "".to_owned())?;
    let mut results = vec![];
    for (_, [number]) in re.captures_iter(&line).map(|c| c.extract()) {
        results.push(number.parse::<i32>().map_err(|e| "NaN")?);
    }
    Ok(format!("{}{}", results[0], results.last().ok_or("Empty list")?).parse::<i32>().map_err(|e| "NaN")?)
}