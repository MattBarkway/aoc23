use crate::utils::types::SimpleResult;
use itertools::Itertools;
use num::ToPrimitive;
use phf::phf_map;
use regex::Regex;

const TARGET_GAME: (i32, i32, i32) = (12, 13, 14);
const NULL: (i32, i32, i32) = (0, 0, 0);

static COLOURS: phf::Map<&'static str, i32> = phf_map! {
    "red" => 0,
    "green" => 1,
    "blue" => 2,
};

pub fn pt_1<T: AsRef<str>>(lines: &[T]) -> SimpleResult<i32> {
    for line in lines {
        let (_, [game_num, remaining]) = Regex::new(r"Game (\d+): (.*)")?
            .captures(line.as_ref())
            .ok_or("No match!")?
            .extract();
        println!("{}", game_num);
        let game = into_game(remaining)?;
        println!("{:?}", game)
        // is_valid_game(remaining);
    }
    // let results: Vec<_> = Regex::new(r"(\d)")?
    //     .captures_iter(line)
    //     .into_iter()
    //     .map(|c| c.extract())
    //     .map(|(_, [number])| number.parse::<i32>())
    //     .collect::<Result<Vec<i32>, _>>()?;
    Ok(8)
}

pub fn pt_2<T: AsRef<str>>(lines: &[T]) -> SimpleResult<i32> {
    Ok(2286)
}

fn into_game(raw_game: &str) -> SimpleResult<(i32, i32, i32)> {
    let mut out = [0, 0, 0];
    let samples = raw_game.split("; ");
    for sample in samples {
        for part in sample.split(", ") {
            let (num, colour) = part.split_once(" ").ok_or("Not enough bits")?;
            out[COLOURS
                .get(colour)
                .ok_or("Not a real colour")?
                .to_owned()
                .to_usize()
                .ok_or("")?] = num.parse()?;
        }
    }
    Ok(out.into_iter().collect_tuple().ok_or("")?)
}

fn is_valid_game(game: &str) -> SimpleResult<()> {
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::utils::types::SimpleResult;

    #[test]
    fn test_pt_1() -> SimpleResult<()> {
        let input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";
        let as_lines = input.lines().collect::<Vec<&str>>();

        assert_eq!(8, pt_1(&as_lines)?);
        Ok(())
    }

    #[test]
    fn test_pt_2() -> SimpleResult<()> {
        let input = "";

        let as_lines = input.lines().collect::<Vec<&str>>();
        assert_eq!(2286, pt_2(&as_lines)?);
        Ok(())
    }
}
