use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader, Error, Lines};
use std::path::Path;

pub(crate) fn load_input(file_name: &str) -> Result<Lines<BufReader<File>>, Error> {
    let file_path = format!("../inputs/{}", file_name);
    Ok(read_lines(file_path)?)
}

fn read_lines<P>(filename: P) -> io::Result<Lines<BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(BufReader::new(file).lines())
}
