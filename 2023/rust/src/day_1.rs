use crate::utils::types::SimpleResult;
use regex::Regex;

pub fn pt_1<T: AsRef<str>>(lines: &[T]) -> SimpleResult<i32> {
    Ok(lines
        .into_iter()
        .map(|line| get_coords(line.as_ref()))
        .collect::<SimpleResult<Vec<_>>>()?
        .iter()
        .sum())
}

fn get_coords(line: &str) -> SimpleResult<i32> {
    let results: Vec<_> = Regex::new(r"(\d)")?
        .captures_iter(line)
        .into_iter()
        .map(|c| c.extract())
        .map(|(_, [number])| number.parse::<i32>())
        .collect::<Result<Vec<i32>, _>>()?;
    Ok(format!("{}{}", results[0], results.last().ok_or("Empty list")?).parse::<i32>()?)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::utils::types::SimpleResult;

    #[test]
    fn test_pt_1() -> SimpleResult<()> {
        let input = "1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet";

        let as_lines = input.lines().collect::<Vec<&str>>();
        assert_eq!(142, pt_1(&as_lines)?);
        Ok(())
    }
}
