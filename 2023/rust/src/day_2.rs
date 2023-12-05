use crate::utils::types::SimpleResult;
use itertools::{max, Itertools};
use num::ToPrimitive;
use phf::phf_map;
use regex::Regex;
use std::ops::Sub;

#[derive(Debug, Copy, Clone, PartialEq, PartialOrd, Eq, Ord)]
struct Sample {
    r: i32,
    g: i32,
    b: i32,
}

impl Sample {
    fn is_valid(self) -> bool {
        !(self.r < 0 || self.g < 0 || self.b < 0)
    }
}

impl Sub for Sample {
    type Output = Self;

    fn sub(self, other: Self) -> Self::Output {
        Self {
            r: self.r - other.r,
            g: self.g - other.g,
            b: self.b - other.b,
        }
    }
}

const MAX_SAMPLE: Sample = Sample {
    r: 12,
    g: 13,
    b: 14,
};
const NULL: Sample = Sample { r: 0, g: 0, b: 0 };

static COLOURS: phf::Map<&'static str, i32> = phf_map! {
    "red" => 0,
    "green" => 1,
    "blue" => 2,
};

pub fn pt_1<T: AsRef<str>>(lines: &[T]) -> SimpleResult<i32> {
    let mut nums = vec![];
    for line in lines {
        let (_, [game_num, remaining]) = Regex::new(r"Game (\d+): (.*)")?
            .captures(line.as_ref())
            .ok_or("No match!")?
            .extract();
        let samples = into_samples(remaining)?;
        if samples
            .into_iter()
            .map(|s| (MAX_SAMPLE - s).is_valid())
            .all(|i| i == true)
        {
            nums.push(game_num.parse::<i32>()?);
        }
    }
    Ok(nums.iter().sum())
}

pub fn pt_2<T: AsRef<str>>(lines: &[T]) -> SimpleResult<i32> {
    let mut max_powers = vec![];
    for line in lines {
        let (_, [game_num, remaining]) = Regex::new(r"Game (\d+): (.*)")?
            .captures(line.as_ref())
            .ok_or("No match!")?
            .extract();
        let samples = into_samples(remaining)?;
        let mut maxes = (vec![], vec![], vec![]);
        let (rs, gs, bs) = samples.into_iter().fold(maxes, |mut acc, i| {
            acc.0.push(i.r);
            acc.1.push(i.g);
            acc.2.push(i.b);
            acc
        });
        let max_game = (
            rs.iter().max().ok_or("")?,
            gs.iter().max().ok_or("")?,
            bs.iter().max().ok_or("")?,
        );
        max_powers.push(max_game.0 * max_game.1 * max_game.2);
    }
    Ok(max_powers.iter().sum())
}

fn into_samples(raw_game: &str) -> SimpleResult<Vec<Sample>> {
    let mut samples = vec![];
    let raw_samples = raw_game.split("; ");
    for raw_sample in raw_samples {
        let mut out = [0, 0, 0];
        for part in raw_sample.split(", ") {
            let (num, colour) = part.split_once(" ").ok_or("Not enough bits")?;
            out[COLOURS
                .get(colour)
                .ok_or("Not a real colour")?
                .to_owned()
                .to_usize()
                .ok_or("")?] = num.parse()?;
        }
        samples.push(Sample {
            r: out[0],
            g: out[1],
            b: out[2],
        })
    }
    Ok(samples)
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
        let input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";

        let as_lines = input.lines().collect::<Vec<&str>>();
        assert_eq!(2286, pt_2(&as_lines)?);
        Ok(())
    }
}
