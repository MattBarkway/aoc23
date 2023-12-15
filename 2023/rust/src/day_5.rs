use crate::utils::types::SimpleResult;
use clap::builder::TypedValueParser;
use itertools::Itertools;
use num::ToPrimitive;
use std::collections::HashMap;

struct RangeMap {
    destination: u32,
    source: u32,
    range: u32,
}

pub fn pt_1<T: AsRef<str>>(lines: &[T]) -> SimpleResult<u32> {
    let seeds = get_seeds(&lines[0].as_ref())?;
    let (maps, ordering) = parse_maps(
        &lines
            .iter()
            .map(AsRef::as_ref)
            .skip(2)
            .collect::<Vec<&str>>(),
    )?;
    let foo = run_maps(maps, seeds, ordering)?;
    Ok(foo.into_iter().min().ok_or("Failed to get min")?)
}

pub fn pt_2<T: AsRef<str>>(lines: &[T]) -> SimpleResult<()> {
    Ok(())
}

fn run_maps(maps: HashMap<String, Vec<RangeMap>>, seeds: Vec<u32>, ordering: Vec<String>) -> SimpleResult<Vec<u32>> {
    let mut finals = vec![];
    for seed in seeds {
        let mut next: u32 = seed;
        for section in &ordering {
            println!("{}", section);
            for map in &maps[section] {
                if map.source <= next && next < (map.source + map.range) {
                    next -= map.source + map.destination + map.range
                }
            }
        }
        finals.push(next);
    }
    Ok(finals)
}

// fn parse_maps(lines: &[&str]) -> SimpleResult<(HashMap<String, Vec<RangeMap>>, Vec<String>)> {
//     let mut iter = lines
//         .iter()
//         // .filter(|i| !i.trim().is_empty())
//         .cloned()
//         .peekable();
//     let mut outmap: HashMap<String, Vec<RangeMap>> = HashMap::new();
//     let mut ordering = vec![];
//     while let Some(row) = &iter.peek().copied() {
//         if row.contains("map:") {
//             ordering.push(row[0..row.len() - 5].to_owned());
//             let mapping_strs: Vec<_> = iter
//                 .by_ref()
//                 .skip(1)
//                 .take_while(|&row| !row.trim().is_empty())
//                 .collect();
//             let numbers: Vec<RangeMap> = mapping_strs
//                 .iter()
//                 .map(|&line| {
//                     line.split_whitespace()
//                         .filter_map(|num| num.parse().ok())
//                         .collect::<Vec<u32>>()
//                 })
//                 .map(|nums| RangeMap {
//                     destination: nums[0],
//                     source: nums[1],
//                     range: nums[2],
//                 })
//                 .collect();
//             outmap.insert(row[0..row.len() - 5].to_owned(), numbers);
//         } else {
//             iter.next();
//         }
//     }
//     Ok((outmap, ordering))
// }

// pub fn get_seeds(line: &str) -> SimpleResult<Vec<u32>> {
//     let (_, seeds_str) = line.split_once(": ").ok_or("")?;
//     Ok(seeds_str
//         .split(" ")
//         .into_iter()
//         .map(|i| i.parse::<u32>())
//         .collect::<Result<Vec<u32>, _>>()?)
// }

#[cfg(test)]
mod tests {
    use super::*;
    use crate::utils::types::SimpleResult;

    #[test]
    fn test_pt_1() -> SimpleResult<()> {
        let input = "seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4";
        let as_lines = input.lines().collect::<Vec<&str>>();

        assert_eq!(35, pt_1(&as_lines)?);
        Ok(())
    }

    #[test]
    fn test_pt_2() -> SimpleResult<()> {
        let input = "";

        let as_lines = input.lines().collect::<Vec<&str>>();
        assert_eq!((), pt_2(&as_lines)?);
        Ok(())
    }
}
