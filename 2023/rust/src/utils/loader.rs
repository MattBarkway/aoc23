use crate::utils::types::SimpleResult;
use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader, Lines};
use std::path::Path;

pub(crate) fn load_input(file_name: &str) -> SimpleResult<Vec<String>> {
    Ok(read_lines(format!("../inputs/{}", file_name))?
        .into_iter()
        .collect::<Result<Vec<String>, _>>()?)
}

fn read_lines<P>(filename: P) -> io::Result<Lines<BufReader<File>>>
where
    P: AsRef<Path>,
{
    Ok(BufReader::new(File::open(filename)?).lines())
}
