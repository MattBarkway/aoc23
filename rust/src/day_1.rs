use crate::utils::loader::load_input;
use crate::utils::types::SimpleResult;
use regex::Regex;

pub fn pt_1() -> SimpleResult<i32> {
    Ok(load_input("1.txt")?
        .map(|line| get_coords(&line?))
        .collect::<SimpleResult<Vec<_>>>()?
        .iter()
        .sum())
}

pub fn pt_2() -> SimpleResult<i32> {
    Ok(load_input("1.txt")?
        .map(|line| get_coords(&line?))
        .collect::<SimpleResult<Vec<_>>>()?
        .iter()
        .sum())
}

fn get_coords(line: &str) -> SimpleResult<i32> {
    let results = Regex::new(r"(\d)")?
        .captures_iter(&line)
        .map(|c| c.extract())
        .map(|(_, [number])| number.parse::<i32>()).collect::<SimpleResult<Vec<_>>>();
    Ok(format!("{}{}", results[0], results.last().ok_or("Empty list")?).parse::<i32>()?)
}
